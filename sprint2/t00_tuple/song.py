def song(versus: tuple, chorus: tuple) -> tuple:
    result = ()

    if isinstance(versus, tuple) and isinstance(chorus, tuple):
        for ver in versus:
            result += ver + chorus
        return result + chorus
