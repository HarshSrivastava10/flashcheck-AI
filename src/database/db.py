from src.database.config import supabase
import bcrypt

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashpwd):
    return bcrypt.checkpw(pwd.encode(), hashpwd.encode())

def check_teacher_exists(username):
    # Check for unique username, returns true when username is already taken
    response = supabase.table('teachers').select("username").eq("username", username).execute()
    return len(response.data) > 0


def create_teacher(username, password, name):

    data = {"username": username, "password": hash_pass(password), "name": name}
    response = supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher['password']):
            return teacher
    return None

def get_all_students():
    response = supabase.table('students').select('*').execute()
    return response.data


def create_student(name, face_embeddings=None, voice_embeddings=None):
    data = {'name': name, 'face_embedding': face_embeddings, 'voice_embedding': voice_embeddings}
    response = supabase.table('students').insert(data).execute()

    return response.data


def create_subject(sub_id, sub_name, sub_section, teacher_id):
    data = {"subject_code": sub_id, "name": sub_name, "section": sub_section, "teacher_id": teacher_id}
    response = supabase.table("subjects").insert(data).execute()

    return response.data


def get_teacher_subjects(teacher_id):
    response = (
        supabase
        .table('subjects')
        .select(
            "*, subject_students(count), attendance_logs(timestamp)"
        )
        .eq("teacher_id", teacher_id)
        .execute()
    )

    subjects = response.data or []
    c = 0
    for sub in subjects:

        sub['total_students'] = (
            sub.get("subject_students", [{}])[0].get('count', 0)
            if sub.get('subject_students')
            else 0
        )

        attendance = sub.get('attendance_logs', [])

        sub['total_classes'] = len(
            set(
                log.get('timestamp')
                for log in attendance
                if log.get('timestamp')
            )
        )
        # print(sub, end="\n")
        sub.pop('subject_students', None)
        sub.pop('attendance_logs', None)
        c+=1
    # print(f"Ran: {c} times")
    
    return subjects


def enroll_student_to_subject(student_id, subject_id):
    data = {'student_id': student_id, 'subject_id': subject_id}
    response = supabase.table('subject_students').insert(data).execute()
    return response.data


def unenroll_student_to_subject(student_id, subject_id):
    response = supabase.table('subject_students').delete().eq('student_id', student_id).eq('subject_id', subject_id).execute()
    return response.data


def get_student_subjects(student_id):
    response = supabase.table('subject_students').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data

def get_student_attendance(student_id):
    response = supabase.table('attendance_logs').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def create_attendance(logs):
    response = supabase.table('attendance_logs').insert(logs).execute()
    return response.data


def get_attendance_for_teacher(teacher_id):
    response = supabase.table('attendance_logs').select('*, subjects!inner(*)').eq('subjects.teacher_id', teacher_id).execute()

    return response.data 