import uuid


def test_get_random_fact(get_fact):
    assert get_fact(request='random').result()


def test_get_parametrized_facts(get_fact):
    assert get_fact(request='random?animal_type=cat&amount=2').result()


def test_get_fact_by_id(get_fact):
    assert get_fact(request='591f98803b90f7150a19c229').result()


def test_get_all_facts(get_fact):
    assert get_fact().result()


def test_get_not_existed_fact(get_fact):
    assert get_fact(request=uuid.uuid4(), desired_status=400).result()
