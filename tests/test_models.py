from models.trainer import Trainer
import pytest


@pytest.fixture
def trainer():
    trainer = Trainer(
        name='Sebastian',
        lastName='Herrera',
        age=21
    )
    return trainer


def test_trainer_to_json_return_json(trainer):
    expected = {
        'name': 'Sebastian',
        'lastName': 'Herrera',
        'age': 21,
    }

    result = trainer.to_json()

    assert result == expected


