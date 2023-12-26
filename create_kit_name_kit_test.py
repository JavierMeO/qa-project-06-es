import sender_stand_request
from data import kit_body

def positive_assert(kit_body):

    user_response = sender_stand_request.create_kit(kit_body)

    assert user_response.status_code == 201
    assert user_response.json()["name"] == kit_body["name"]


def negative_assert_symbol(kit_body):

    response = sender_stand_request.create_kit(kit_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == 'El nombre debe contener sólo letras latino,' \
                                         'un espacio y un guión. De 2 a 15 caracteres'

def negative_assert_no_name(kit_body):

    response = sender_stand_request.create_kit(kit_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

#El número permitido de caracteres (1):
def test_create_kit_1_letter_in_name_is_allowed():
    positive_assert(kit_body.kit_body_1)

#El número permitido de caracteres (511):
def test_create_kit_511_letters_in_name_is_allowed():
    positive_assert(kit_body.kit_body_2)
#El número de caracteres es menor que la cantidad permitida (0):
def test_create_kit_0_letter0_in_name_is_forbidden():
    negative_assert_no_name(kit_body.kit_body_3)

#El número de caracteres es mayor que la cantidad permitida (512):
def test_create_kit_512_letter_in_name_is_forbidden():
    negative_assert_symbol(kit_body.kit_body_4)
#Se permiten caracteres especiales:
def test_create_kit_special_characters_in_name_is_allowed():
    positive_assert(kit_body.kit_body_5)

#Se permiten espacios:
def test_create_kit_spaces_in_name_are_allowed():
    positive_assert(kit_body.kit_body_6)

#Se permiten números:
def test_create_kit_numbers_in_name_are_allowed():
    positive_assert(kit_body.kit_body_7)

#El parámetro no se pasa en la solicitud:
def test_create_kit_empty_in_name_is_forbidden():
    negative_assert_no_name(kit_body.kit_body_8)

#Se ha pasado un tipo de parámetro diferente (número):
def test_create_kit_int_in_name_is_forbidden():
    negative_assert_symbol(kit_body.kit_body_9)