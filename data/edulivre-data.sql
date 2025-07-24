INSERT INTO user (uuid, name, email, phone, password)
VALUES
    ('3c57ec2a-c51d-4245-b486-bb3c0bbbaefb', 'Carlos Silva', 'carlos.silva@example.com', '11976543210', 'Carlos@2023*'),
    ('d955c0d0-fe5f-407c-a41e-06c352f984db', 'Daniela Rocha', 'daniela.rocha@example.com', '11965432109', 'Daniela@2023$'),
    ('c7f43cc0-cebb-458f-9cb4-1462f79d5349', 'Eduardo Alves', 'eduardo.alves@example.com', '11954321098', 'Eduardo@2023%'),
    ('9495773b-59c6-461a-bef3-7f8ab77a7fd2', 'Fernanda Melo', 'fernanda.melo@example.com', '11943210987', 'Fernanda@2023&'),
    ('e6b25c37-9735-4042-9a17-26a0a5d4898a', 'Gustavo Ramos', 'gustavo.ramos@example.com', '11932109876', 'Gustavo@2023?'),
    ('18be527b-0346-4980-a807-b5f0b4e45829', 'Helena Castro', 'helena.castro@example.com', '11921098765', 'Helena@2023+'),
    ('56faef37-6ac4-4c0f-bfde-660c0021408f', 'Igor Martins', 'igor.martins@example.com', '11910987654', 'Igor@2023='),
    ('bf78e5c8-eb06-44d6-a623-cbf1fbbed413', 'Juliana Dias', 'juliana.dias@example.com', '11999876543', 'Juliana@2023_'),
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', 'Kleber Nunes', 'kleber.nunes@example.com', '11988765432', 'Kleber@2023-'),
    ('c014bffe-4dba-47f0-a71f-5fb3956d0305', 'Larissa Tavares', 'larissa.tavares@example.com', '11977654321', 'Larissa@2023@'),
    ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', 'Marcelo Pinto', 'marcelo.pinto@example.com', '11966543210', 'Marcelo@2023^'),
    ('ed59fc5f-2f3c-4e76-930c-27210c5549bb', 'Natalia Gomes', 'natalia.gomes@example.com', '11955432109', 'Natalia@2023~'),
    ('2b01591e-a7b5-463c-996d-e174c79ef6f8', 'Otávio Fernandes', 'otavio.fernandes@example.com', '11944321098', 'Otavio@2023|'),
    ('9dbc0b2f-ea4c-4275-ae46-39be78304014', 'Paula Ribeiro', 'paula.ribeiro@example.com', '11933210987', 'Paula@2023\\'),
    ('563f0581-3429-4bab-bc9e-b0760081862b', 'Rafael Teixeira', 'rafael.teixeira@example.com', '11922109876', 'Rafael@2023`'),
    ('96017375-2da5-49a7-8e1b-4fe845a1575a', 'Sabrina Costa', 'sabrina.costa@example.com', '11911098765', 'Sabrina@2023!'),
    ('3379e036-f462-4b49-b46f-167742af6190', 'Thiago Barros', 'thiago.barros@example.com', '11900987654', 'Thiago@2023#'),
    ('79854c84-e5c1-4259-aa84-f665d2891efa', 'Vanessa Moura', 'vanessa.moura@example.com', '11988877766', 'Vanessa@2023!'),
    ('8f349cfe-bd55-4c8f-88f1-dffc3e12d37c', 'Ana Souza', 'ana.souza@example.com', '11987654321', 'Ana@2023#'),
    ('883927eb-436d-4d6a-ae82-a01bfb9e673b', 'Bruno Lima', 'bruno.lima@google.com', '11986543210', 'Bruno@2023!');

INSERT INTO teacher (uuid, degree, specialties) VALUES
    ('8f349cfe-bd55-4c8f-88f1-dffc3e12d37c', 'Doutorado em Educação', 'Didática e Metodologias Ativas'),
    ('883927eb-436d-4d6a-ae82-a01bfb9e673b', 'Mestrado em Letras', 'Literatura Brasileira e Crítica Literária'),
    ('3c57ec2a-c51d-4245-b486-bb3c0bbbaefb', 'Pós-graduação em Ciência da Computação', 'Inteligência Artificial e Machine Learning'),
    ('d955c0d0-fe5f-407c-a41e-06c352f984db', 'Bacharelado em Artes Cênicas', 'Teatro Musical e Expressão Corporal'),
    ('c7f43cc0-cebb-458f-9cb4-1462f79d5349', 'Licenciatura em Matemática', 'Cálculo Avançado e Geometria Analítica'),
    ('9495773b-59c6-461a-bef3-7f8ab77a7fd2', 'Mestrado em História', 'História Contemporânea e Arqueologia'),
    ('e6b25c37-9735-4042-9a17-26a0a5d4898a', 'Doutorado em Engenharia Ambiental', 'Sustentabilidade e Energias Renováveis'),
    ('18be527b-0346-4980-a807-b5f0b4e45829', 'Pós-graduação em Psicopedagogia', 'Dificuldades de Aprendizagem e Inclusão'),
    ('56faef37-6ac4-4c0f-bfde-660c0021408f', 'Bacharelado em Música', 'Composição Musical e Regência'),
    ('bf78e5c8-eb06-44d6-a623-cbf1fbbed413', 'Licenciatura em Biologia', 'Genética e Biotecnologia');

INSERT INTO student (uuid, grade_level, interests) VALUES
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', 'Fundamental', 'Ciências e Tecnologia'),
    ('c014bffe-4dba-47f0-a71f-5fb3956d0305', 'Médio', 'Matemática e Lógica'),
    ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', 'Superior', 'Música e Dança'),
    ('ed59fc5f-2f3c-4e76-930c-27210c5549bb', 'Fundamental', 'Esportes e Bem-estar'),
    ('2b01591e-a7b5-463c-996d-e174c79ef6f8', 'Superior', 'Matemática e Lógica'),
    ('9dbc0b2f-ea4c-4275-ae46-39be78304014', 'Médio', 'Empreendedorismo e Negócios'),
    ('563f0581-3429-4bab-bc9e-b0760081862b', 'Fundamental', 'Esportes e Bem-estar'),
    ('96017375-2da5-49a7-8e1b-4fe845a1575a', 'Fundamental', 'Música e Dança'),
    ('3379e036-f462-4b49-b46f-167742af6190', 'Fundamental', 'Idiomas e Comunicação'),
    ('79854c84-e5c1-4259-aa84-f665d2891efa', 'Médio', 'Música e Dança');

INSERT INTO workshop (uuid, title, category, address, description, capacity, start_date, end_date, duration, teacher_uuid) VALUES ('19e56733-557d-4ec1-9f1f-cbe2c0ccd3f1', 'Didática Inovadora para o Século XXI', 'Educação', 'Online', 'Explore novas abordagens didáticas e metodologias ativas para engajar alunos.', 25, '2025-09-01 09:00:00', '2025-09-01 17:00:00', '08:00:00', '8f349cfe-bd55-4c8f-88f1-dffc3e12d37c');
INSERT INTO workshop (uuid, title, category, address, description, capacity, start_date, end_date, duration, teacher_uuid) VALUES ('e0febe54-f389-4cd8-b41e-d45b0e0a5692', 'A Arte de Contar Histórias na Literatura Brasileira', 'Literatura', 'Centro Cultural da Cidade, Sala 3', 'Um mergulho profundo nas técnicas narrativas dos grandes mestres da literatura nacional.', 20, '2025-10-05 14:00:00', '2025-10-05 18:00:00', '04:00:00', '883927eb-436d-4d6a-ae82-a01bfb9e673b');
INSERT INTO workshop (uuid, title, category, address, description, capacity, start_date, end_date, duration, teacher_uuid) VALUES ('065d1816-c90f-4fb5-8264-498572a3bac0', 'Introdução à Inteligência Artificial com Python', 'Tecnologia', 'Campus Universitário, Lab de IA', 'Aprenda os fundamentos da IA e Machine Learning com exemplos práticos em Python.', 30, '2025-11-10 10:00:00', '2025-11-12 17:00:00', '2 days', '3c57ec2a-c51d-4245-b486-bb3c0bbbaefb');
INSERT INTO workshop (uuid, title, category, address, description, capacity, start_date, end_date, duration, teacher_uuid) VALUES ('84f5a7f5-ac8c-49d4-8bb3-5b1164f1c132', 'Expressão Corporal e Teatro Musical', 'Artes Cênicas', 'Teatro Municipal, Palco Principal', 'Desenvolva sua presença de palco e habilidades de expressão para o teatro musical.', 15, '2025-09-15 18:00:00', '2025-09-15 22:00:00', '04:00:00', 'd955c0d0-fe5f-407c-a41e-06c352f984db');
INSERT INTO workshop (uuid, title, category, address, description, capacity, start_date, end_date, duration, teacher_uuid) VALUES ('ea62b956-c310-4331-bb66-c061317339c4', 'Desvendando o Cálculo Avançado', 'Matemática', 'Online', 'Revisão e aprofundamento em tópicos de cálculo diferencial e integral avançado.', 40, '2025-10-20 09:00:00', '2025-10-24 12:00:00', '4 days', 'c7f43cc0-cebb-458f-9cb4-1462f79d5349');
INSERT INTO workshop (uuid, title, category, address, description, capacity, start_date, end_date, duration, teacher_uuid) VALUES ('c6d0c1d4-124c-4bf9-b24a-a9d5dc0f98c7', 'Arqueologia e Sociedades Antigas', 'História', 'Museu de História Natural, Auditório', 'Uma jornada pelas civilizações antigas e os métodos da arqueologia moderna.', 22, '2025-11-03 13:00:00', '2025-11-03 17:00:00', '04:00:00', '9495773b-59c6-461a-bef3-7f8ab77a7fd2');
INSERT INTO workshop (uuid, title, category, address, description, capacity, start_date, end_date, duration, teacher_uuid) VALUES ('51f4e6ce-e2ac-4b9e-b147-4dc603f897cc', 'Sustentabilidade e Energias Renováveis', 'Meio Ambiente', 'Parque Tecnológico, Sala Verde', 'Explore as últimas inovações em energias limpas e práticas sustentáveis.', 28, '2025-12-01 09:00:00', '2025-12-02 17:00:00', '2 days', 'e6b25c37-9735-4042-9a17-26a0a5d4898a');
INSERT INTO workshop (uuid, title, category, address, description, capacity, start_date, end_date, duration, teacher_uuid) VALUES ('de420e6a-54a6-4962-908b-a121b0e6f8fa', 'Inclusão e Dificuldades de Aprendizagem', 'Psicopedagogia', 'Clínica de Apoio Educacional, Sala 1', 'Estratégias e ferramentas para apoiar alunos com dificuldades de aprendizagem.', 18, '2025-09-25 10:00:00', '2025-09-25 16:00:00', '06:00:00', '18be527b-0346-4980-a807-b5f0b4e45829');
INSERT INTO workshop (uuid, title, category, address, description, capacity, start_date, end_date, duration, teacher_uuid) VALUES ('fe97ad47-2139-4663-a509-92b56cdaa95f', 'Composição Musical: Do Conceito à Partitura', 'Música', 'Conservatório de Música, Sala de Ensaios', 'Aprenda os princípios da composição musical e crie suas próprias obras.', 12, '2025-10-10 15:00:00', '2025-10-10 19:00:00', '04:00:00', '56faef37-6ac4-4c0f-bfde-660c0021408f');
INSERT INTO workshop (uuid, title, category, address, description, capacity, start_date, end_date, duration, teacher_uuid) VALUES ('8f00c003-b9ab-459f-ab17-ea06615fc806', 'Biotecnologia e o Futuro da Genética', 'Biologia', 'Instituto de Pesquisas Biomédicas, Auditório', 'Descubra os avanços e aplicações da biotecnologia na área da genética.', 25, '2025-11-18 09:00:00', '2025-11-18 17:00:00', '08:00:00', 'bf78e5c8-eb06-44d6-a623-cbf1fbbed413');

INSERT INTO lesson (uuid, title, description, class_type, status, recording_url, teacher_uuid, workshop_uuid) VALUES
    ('a0e1b2c3-d4e5-4f67-8901-234567890abc', 'Fundamentos de IA e Machine Learning', 'Visão geral dos conceitos básicos de Inteligência Artificial e Machine Learning.', 'Teórica', 'Concluída', 'https://example.com/recordings/ia_fundamentos.mp4', '3c57ec2a-c51d-4245-b486-bb3c0bbbaefb', '065d1816-c90f-4fb5-8264-498572a3bac0'),
    ('b1c2d3e4-f5a6-7b89-0123-4567890abcde', 'Introdução ao Python para IA', 'Revisão dos conceitos essenciais de Python focados em ciência de dados e IA.', 'Prática', 'Concluída', 'https://example.com/recordings/python_ia.mp4', '3c57ec2a-c51d-4245-b486-bb3c0bbbaefb', '065d1816-c90f-4fb5-8264-498572a3bac0'),
    ('c2d3e4f5-a6b7-8c90-1234-567890abcdef', 'Regressão Linear e Polinomial', 'Exploração de modelos de regressão linear e polinomial com exemplos práticos.', 'Teórica/Prática', 'Concluída', 'https://example.com/recordings/regressao.mp4', '3c57ec2a-c51d-4245-b486-bb3c0bbbaefb', '065d1816-c90f-4fb5-8264-498572a3bac0'),
    ('d3e4f5a6-b7c8-9d01-2345-67890abcdef0', 'Classificação com Regressão Logística', 'Entendimento e aplicação da regressão logística para problemas de classificação.', 'Teórica/Prática', 'Concluída', 'https://example.com/recordings/classificacao.mp4', '3c57ec2a-c51d-4245-b486-bb3c0bbbaefb', '065d1816-c90f-4fb5-8264-498572a3bac0'),
    ('e4f5a6b7-c8d9-0e12-3456-7890abcdef01', 'Árvores de Decisão e Random Forest', 'Construção e otimização de árvores de decisão e florestas aleatórias.', 'Prática', 'Concluída', 'https://example.com/recordings/arvores_decisao.mp4', '3c57ec2a-c51d-4245-b486-bb3c0bbbaefb', '065d1816-c90f-4fb5-8264-498572a3bac0'),
    ('f5a6b7c8-d9e0-1f23-4567-890abcdef012', 'Máquinas de Vetores de Suporte (SVM)', 'Teoria e aplicação de SVMs para classificação e regressão.', 'Teórica/Prática', 'Concluída', 'https://example.com/recordings/svm.mp4', '3c57ec2a-c51d-4245-b486-bb3c0bbbaefb', '065d1816-c90f-4fb5-8264-498572a3bac0'),
    ('a6b7c8d9-e0f1-2a34-5678-90abcdef0123', 'Introdução às Redes Neurais', 'Primeiros passos no mundo das redes neurais e seus fundamentos.', 'Teórica', 'Concluída', 'https://example.com/recordings/redes_neurais.mp4', '3c57ec2a-c51d-4245-b486-bb3c0bbbaefb', '065d1816-c90f-4fb5-8264-498572a3bac0'),
    ('b7c8d9e0-f1a2-3b45-6789-0abcdef01234', 'Deep Learning com TensorFlow/Keras', 'Construção de modelos de Deep Learning usando as bibliotecas TensorFlow e Keras.', 'Prática', 'Em Andamento', 'https://example.com/recordings/deep_learning.mp4', '3c57ec2a-c51d-4245-b486-bb3c0bbbaefb', '065d1816-c90f-4fb5-8264-498572a3bac0'),
    ('c8d9e0f1-a2b3-4c56-7890-abcdef012345', 'Processamento de Linguagem Natural (PNL)', 'Introdução à PNL e suas aplicações, como análise de sentimento.', 'Teórica/Prática', 'Pendente', NULL, '3c57ec2a-c51d-4245-b486-bb3c0bbbaefb', '065d1816-c90f-4fb5-8264-498572a3bac0'),
    ('d9e0f1a2-b3c4-5d67-8901-234567890abc', 'Visão Computacional Básica', 'Conceitos fundamentais de visão computacional e reconhecimento de imagens.', 'Teórica/Prática', 'Pendente', NULL, '3c57ec2a-c51d-4245-b486-bb3c0bbbaefb', '065d1816-c90f-4fb5-8264-498572a3bac0');

INSERT INTO participate (student_uuid, workshop_uuid) VALUES
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', '19e56733-557d-4ec1-9f1f-cbe2c0ccd3f1'),
    ('c014bffe-4dba-47f0-a71f-5fb3956d0305', 'e0febe54-f389-4cd8-b41e-d45b0e0a5692'),
    ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', '065d1816-c90f-4fb5-8264-498572a3bac0'),
    ('ed59fc5f-2f3c-4e76-930c-27210c5549bb', '84f5a7f5-ac8c-49d4-8bb3-5b1164f1c132'),
    ('2b01591e-a7b5-463c-996d-e174c79ef6f8', 'ea62b956-c310-4331-bb66-c061317339c4'),
    ('9dbc0b2f-ea4c-4275-ae46-39be78304014', 'c6d0c1d4-124c-4bf9-b24a-a9d5dc0f98c7'),
    ('563f0581-3429-4bab-bc9e-b0760081862b', '51f4e6ce-e2ac-4b9e-b147-4dc603f897cc'),
    ('96017375-2da5-49a7-8e1b-4fe845a1575a', 'de420e6a-54a6-4962-908b-a121b0e6f8fa'),
    ('3379e036-f462-4b49-b46f-167742af6190', 'fe97ad47-2139-4663-a509-92b56cdaa95f'),
    ('79854c84-e5c1-4259-aa84-f665d2891efa', '8f00c003-b9ab-459f-ab17-ea06615fc806');

INSERT INTO history (user_uuid, action) VALUES
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', 'Fez login no sistema.'),
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', 'Pesquisou por workshops na categoria "Tecnologia".'),
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', 'Visualizou os detalhes do workshop "Introdução à Inteligência Artificial com Python".'),
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', 'Inscreveu-se no workshop "Didática Inovadora para o Século XXI".'),
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', 'Atualizou as informações do seu perfil.'),
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', 'Visualizou o histórico de participação em workshops.'),
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', 'Baixou o certificado do workshop "Sustentabilidade e Energias Renováveis".'),
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', 'Alterou a senha de acesso.'),
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', 'Cancelou a inscrição no workshop "A Arte de Contar Histórias na Literatura Brasileira".'),
    ('c7f4b234-5d6f-4e23-a12b-dc319f9e3a6a', 'Fez logout do sistema.');

INSERT INTO frequency (student_uuid, lesson_uuid, status) VALUES ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', 'a0e1b2c3-d4e5-4f67-8901-234567890abc', 'Presente');
INSERT INTO frequency (student_uuid, lesson_uuid, status) VALUES ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', 'b1c2d3e4-f5a6-7b89-0123-4567890abcde', 'Presente');
INSERT INTO frequency (student_uuid, lesson_uuid, status) VALUES ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', 'c2d3e4f5-a6b7-8c90-1234-567890abcdef', 'Ausente');
INSERT INTO frequency (student_uuid, lesson_uuid, status) VALUES ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', 'd3e4f5a6-b7c8-9d01-2345-67890abcdef0', 'Presente');
INSERT INTO frequency (student_uuid, lesson_uuid, status) VALUES ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', 'e4f5a6b7-c8d9-0e12-3456-7890abcdef01', 'Justificado');
INSERT INTO frequency (student_uuid, lesson_uuid, status) VALUES ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', 'f5a6b7c8-d9e0-1f23-4567-890abcdef012', 'Presente');
INSERT INTO frequency (student_uuid, lesson_uuid, status) VALUES ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', 'a6b7c8d9-e0f1-2a34-5678-90abcdef0123', 'Presente');
INSERT INTO frequency (student_uuid, lesson_uuid, status) VALUES ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', 'b7c8d9e0-f1a2-3b45-6789-0abcdef01234', 'Ausente');
INSERT INTO frequency (student_uuid, lesson_uuid, status) VALUES ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', 'c8d9e0f1-a2b3-4c56-7890-abcdef012345', 'Presente');
INSERT INTO frequency (student_uuid, lesson_uuid, status) VALUES ('7f49cd49-a6cb-4fa6-94b0-3005fe230277', 'd9e0f1a2-b3c4-5d67-8901-234567890abc', 'Presente');
