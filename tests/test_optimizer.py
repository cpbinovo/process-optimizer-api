from optimizerapi import optimizer

def test_first_sample():
    Xi = [0.01]
    yi = 1
    result = optimizer.run(params="{}", Xi=Xi, yi=yi)
    print(result)
    assert "plots" in result