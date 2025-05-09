USE `pyrano`;

INSERT INTO site (station, latitude, longitude, elevation, description, created_at)
VALUES (
    'goacf',
    41.663632,
    -4.70586,
    712.00,
    'Facultad de Ciencias',
    '2023-01-01 00:00:00'
);

INSERT INTO site (station, latitude, longitude, elevation, description, created_at)
VALUES (
    'ies_jjl',
    41.6329100,
    -4.7648600,
    730.00,
    'IES José Jiménez Lozano',
    '2023-01-01 00:00:00'
);

INSERT INTO site (station, latitude, longitude, elevation, description, created_at)
VALUES (
    'cee_1',
    41.6136712,
    -4.7537823,
    695.00,
    'Centro de Educación Especial Nº1',
    '2023-01-01 00:00:00'
);

INSERT INTO site (station, latitude, longitude, elevation, description, created_at)
VALUES (
    'derecho',
    41.6524318,
    -4.7217346,
    708.00,
    'Facultad de Derecho',
    '2023-01-01 00:00:00'
);

INSERT INTO instrument (instr_id, type, created_at)
VALUES (
    'Rad001',
    'SMP10-V',
    '2023-01-01 00:00:00'
);

INSERT INTO instrument (instr_id, type, created_at)
VALUES (
    'Rad002',
    'SMP10-V',
    '2023-01-01 00:00:00'
);

INSERT INTO instrument (instr_id, type, created_at)
VALUES (
    'Rad003',
    'SMP10-V',
    '2023-01-01 00:00:00'
);

INSERT INTO instrument (instr_id, type, created_at)
VALUES (
    'Rad004',
    'SMP10-V',
    '2023-01-01 00:00:00'
);

INSERT INTO installation (station, instr_id, install_time, radtype)
VALUES (
    'goacf',
    'Rad001',
    '2023-05-22 09:00:00',
    'global'
);

INSERT INTO installation (station, instr_id, install_time, radtype)
VALUES (
    'ies_jjl',
    'Rad002',
    '2023-09-20 09:00:00',
    'global'
);

INSERT INTO installation (station, instr_id, install_time, radtype)
VALUES (
    'cee_1',
    'Rad003',
    '2025-02-18 09:00:00',
    'global'
);

INSERT INTO installation (station, instr_id, install_time, radtype)
VALUES (
    'derecho',
    'Rad004',
    '2024-10-21 09:00:00',
    'global'
);
