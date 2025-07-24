CREATE TYPE grade_type AS ENUM ('Fundamental', 'Médio', 'Superior');
CREATE TYPE workshop_status AS ENUM ('Ativo', 'Inativo', 'Cancelado');
CREATE TYPE attendance_status AS ENUM ('Presente', 'Ausente', 'Justificado');

CREATE TABLE user (
    uuid UUID DEFAULT gen_random_uuid() UNIQUE,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE teacher (
    uuid UUID NOT NULL UNIQUE REFERENCES user(uuid),
    degree TEXT,
    specialties TEXT
);

CREATE TABLE student (
    uuid UUID NOT NULL UNIQUE REFERENCES user(uuid),
    grade_level grade_type NOT NULL,
    interests TEXT
);

CREATE TABLE workshop (
    uuid UUID DEFAULT gen_random_uuid() UNIQUE,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    address TEXT,
    description TEXT,
    capacity INTEGER,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    duration INTERVAL,
    teacher_uuid UUID NOT NULL REFERENCES teacher(uuid)
);

CREATE TABLE participate (
    uuid UUID DEFAULT gen_random_uuid() UNIQUE,
    student_uuid UUID NOT NULL REFERENCES student(uuid),
    workshop_uuid UUID NOT NULL REFERENCES workshop(uuid),
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE lesson (
    uuid UUID DEFAULT gen_random_uuid() UNIQUE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    class_type VARCHAR(50),
    status VARCHAR(50),
    recording_url TEXT,
    teacher_uuid UUID NOT NULL REFERENCES teacher(uuid),
    workshop_uuid UUID NOT NULL REFERENCES workshop(uuid)
);

CREATE TABLE frequency (
    uuid UUID DEFAULT gen_random_uuid() UNIQUE,
    student_uuid UUID NOT NULL REFERENCES student(uuid),
    lesson_uuid UUID NOT NULL REFERENCES lesson(uuid),
    status attendance_status NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE history (
    uuid UUID DEFAULT gen_random_uuid() UNIQUE,
    user_uuid UUID REFERENCES user(uuid),
    action TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
