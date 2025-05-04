/* Define diseases and their symptoms */
disease(flu) :- has(fever), has(cough), has(fatigue).
disease(cold) :- has(runny_nose), has(cough), not_has(fever).
disease(allergies) :- has(runny_nose), has(sneezing), not_has(fever).
disease(strep_throat) :- has(sore_throat), has(fever), not_has(cough).

/* Store answers dynamically */
:- dynamic answer/2.

/* Check if a symptom is present */
has(Symptom) :-
    answer(Symptom, yes),   /* Already answered yes */
    true.
has(Symptom) :-
    answer(Symptom, no),    /* Already answered no */
    fail.
has(Symptom) :-
    write('Does the patient have '), write(Symptom), write('? (yes/no) '),
    read(Response),
    (Response = yes ; Response = no),  /* Ensure valid input */
    asserta(answer(Symptom, Response)), /* Store answer */
    Response = yes.

/* Check if a symptom is not present */
not_has(Symptom) :-
    answer(Symptom, no),    /* Already answered no */
    true.
not_has(Symptom) :-
    answer(Symptom, yes),   /* Already answered yes */
    fail.
not_has(Symptom) :-
    write('Does the patient have '), write(Symptom), write('? (yes/no) '),
    read(Response),
    (Response = yes ; Response = no),  /* Ensure valid input */
    asserta(answer(Symptom, Response)), /* Store answer */
    Response = no.

/* Diagnose a disease */
diagnose(Disease) :-
    disease(Disease),
    write('Possible diagnosis: '), write(Disease), nl.

/* Clear all stored answers */
clear :-
    retractall(answer(_, _)).