from pipeline.retrain import retrain_model


def test_training():

    metrics = retrain_model()

    assert metrics["accuracy"] >= 0.90