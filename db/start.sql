USE `pyrano`;

INSERT INTO site (station, latitude, longitude, elevation, description, created_at)
VALUES (
    'ies_jjl',
    41.6329100,
    -4.7648600,
    725.00,
    'IES José Jiménez Lozano',
    '2023-09-20 09:00:00'
);

INSERT INTO instrument (instr_id, type, created_at)
VALUES (
    'Rad002',
    'SMP10-V',
    '2023-09-20 09:00:00'
);

INSERT INTO installation (station, instr_id, install_time, radtype)
VALUES (
    'ies_jjl',
    'Rad002',
    '2023-09-20 09:00:00',
    'global'
);
