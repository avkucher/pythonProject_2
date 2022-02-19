import json


def load_candidates():

    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)

    return candidates


def get_candidates_all(): # все кандидаты
    return load_candidates()


def get_candidate_by_id(uid): # поиск кандидатов по id

    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate


def get_candidates_by_skill(skill): # поиск кандидатов по умениям

    candidates = load_candidates()
    skilled_candidates = []
    skill_lower = skill.lower()

    for candidate in candidates:
        candidate_skill = candidate['skills'].lower().split(', ')
        if skill_lower in candidate_skill:
            skilled_candidates.append(candidate)
    return skilled_candidates


