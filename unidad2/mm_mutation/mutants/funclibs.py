
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:09:17 2021

@author: nadia
"""


import numpy as np
import pandas as pd

_ENT = -1 / np.log2(2)


def x_risso_candidate_entropy__mutmut_orig(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_1(windows_size):
    if windows_size < 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_2(windows_size):
    if windows_size <= 1:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_3(windows_size):
    if windows_size <= 0:
        raise ValueError("XX'windows_size' must be > 0XX")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_4(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(1.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_5(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 2.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_6(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size - 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_7(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 2)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_8(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0,)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_9(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = None

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_10(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = None
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_11(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[1] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_12(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[None] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_13(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = None
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_14(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[+1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_15(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-2] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_16(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[None] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_17(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 2 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_18(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 + epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_19(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = None

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_20(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability / np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_21(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(None)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_22(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = None
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_23(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (2 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_24(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 + loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_25(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) / np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_26(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(2 - loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_27(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 + loss_probability)

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_28(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = None

    modificated_entropy = _ENT * (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_29(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT / (first_part + second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_30(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = _ENT * (first_part - second_part)
    return modificated_entropy, loss_probability


def x_risso_candidate_entropy__mutmut_31(windows_size):
    if windows_size <= 0:
        raise ValueError("'windows_size' must be > 0")

    loss_probability = np.linspace(0.0, 1.0, num=windows_size + 1)

    # Se corrigen probabilidades porque el cálculo de la entropía trabaja con
    # logaritmo y el logaritmo de cero no puede calcularse
    epsilon = np.finfo(loss_probability.dtype).eps
    loss_probability[0] = epsilon
    loss_probability[-1] = 1 - epsilon

    # Calcula entropy
    first_part = loss_probability * np.log2(loss_probability)
    second_part = (1 - loss_probability) * np.log2(1 - loss_probability)

    modificated_entropy = None
    return modificated_entropy, loss_probability

x_risso_candidate_entropy__mutmut_mutants = {
'x_risso_candidate_entropy__mutmut_1': x_risso_candidate_entropy__mutmut_1, 
    'x_risso_candidate_entropy__mutmut_2': x_risso_candidate_entropy__mutmut_2, 
    'x_risso_candidate_entropy__mutmut_3': x_risso_candidate_entropy__mutmut_3, 
    'x_risso_candidate_entropy__mutmut_4': x_risso_candidate_entropy__mutmut_4, 
    'x_risso_candidate_entropy__mutmut_5': x_risso_candidate_entropy__mutmut_5, 
    'x_risso_candidate_entropy__mutmut_6': x_risso_candidate_entropy__mutmut_6, 
    'x_risso_candidate_entropy__mutmut_7': x_risso_candidate_entropy__mutmut_7, 
    'x_risso_candidate_entropy__mutmut_8': x_risso_candidate_entropy__mutmut_8, 
    'x_risso_candidate_entropy__mutmut_9': x_risso_candidate_entropy__mutmut_9, 
    'x_risso_candidate_entropy__mutmut_10': x_risso_candidate_entropy__mutmut_10, 
    'x_risso_candidate_entropy__mutmut_11': x_risso_candidate_entropy__mutmut_11, 
    'x_risso_candidate_entropy__mutmut_12': x_risso_candidate_entropy__mutmut_12, 
    'x_risso_candidate_entropy__mutmut_13': x_risso_candidate_entropy__mutmut_13, 
    'x_risso_candidate_entropy__mutmut_14': x_risso_candidate_entropy__mutmut_14, 
    'x_risso_candidate_entropy__mutmut_15': x_risso_candidate_entropy__mutmut_15, 
    'x_risso_candidate_entropy__mutmut_16': x_risso_candidate_entropy__mutmut_16, 
    'x_risso_candidate_entropy__mutmut_17': x_risso_candidate_entropy__mutmut_17, 
    'x_risso_candidate_entropy__mutmut_18': x_risso_candidate_entropy__mutmut_18, 
    'x_risso_candidate_entropy__mutmut_19': x_risso_candidate_entropy__mutmut_19, 
    'x_risso_candidate_entropy__mutmut_20': x_risso_candidate_entropy__mutmut_20, 
    'x_risso_candidate_entropy__mutmut_21': x_risso_candidate_entropy__mutmut_21, 
    'x_risso_candidate_entropy__mutmut_22': x_risso_candidate_entropy__mutmut_22, 
    'x_risso_candidate_entropy__mutmut_23': x_risso_candidate_entropy__mutmut_23, 
    'x_risso_candidate_entropy__mutmut_24': x_risso_candidate_entropy__mutmut_24, 
    'x_risso_candidate_entropy__mutmut_25': x_risso_candidate_entropy__mutmut_25, 
    'x_risso_candidate_entropy__mutmut_26': x_risso_candidate_entropy__mutmut_26, 
    'x_risso_candidate_entropy__mutmut_27': x_risso_candidate_entropy__mutmut_27, 
    'x_risso_candidate_entropy__mutmut_28': x_risso_candidate_entropy__mutmut_28, 
    'x_risso_candidate_entropy__mutmut_29': x_risso_candidate_entropy__mutmut_29, 
    'x_risso_candidate_entropy__mutmut_30': x_risso_candidate_entropy__mutmut_30, 
    'x_risso_candidate_entropy__mutmut_31': x_risso_candidate_entropy__mutmut_31
}

def risso_candidate_entropy(*args, **kwargs):
    result = _mutmut_trampoline(x_risso_candidate_entropy__mutmut_orig, x_risso_candidate_entropy__mutmut_mutants, *args, **kwargs)
    return result 

risso_candidate_entropy.__signature__ = _mutmut_signature(x_risso_candidate_entropy__mutmut_orig)
x_risso_candidate_entropy__mutmut_orig.__name__ = 'x_risso_candidate_entropy'




def x_argnearest__mutmut_orig(arr, v):
    diff = np.abs(np.subtract(arr, v))
    idx = np.argmin(diff)
    return idx


def x_argnearest__mutmut_1(arr, v):
    diff = np.abs(np.subtract(None, v))
    idx = np.argmin(diff)
    return idx


def x_argnearest__mutmut_2(arr, v):
    diff = np.abs(np.subtract(arr, None))
    idx = np.argmin(diff)
    return idx


def x_argnearest__mutmut_3(arr, v):
    diff = np.abs(np.subtract( v))
    idx = np.argmin(diff)
    return idx


def x_argnearest__mutmut_4(arr, v):
    diff = np.abs(np.subtract(arr,))
    idx = np.argmin(diff)
    return idx


def x_argnearest__mutmut_5(arr, v):
    diff = None
    idx = np.argmin(diff)
    return idx


def x_argnearest__mutmut_6(arr, v):
    diff = np.abs(np.subtract(arr, v))
    idx = np.argmin(None)
    return idx


def x_argnearest__mutmut_7(arr, v):
    diff = np.abs(np.subtract(arr, v))
    idx = None
    return idx

x_argnearest__mutmut_mutants = {
'x_argnearest__mutmut_1': x_argnearest__mutmut_1, 
    'x_argnearest__mutmut_2': x_argnearest__mutmut_2, 
    'x_argnearest__mutmut_3': x_argnearest__mutmut_3, 
    'x_argnearest__mutmut_4': x_argnearest__mutmut_4, 
    'x_argnearest__mutmut_5': x_argnearest__mutmut_5, 
    'x_argnearest__mutmut_6': x_argnearest__mutmut_6, 
    'x_argnearest__mutmut_7': x_argnearest__mutmut_7
}

def argnearest(*args, **kwargs):
    result = _mutmut_trampoline(x_argnearest__mutmut_orig, x_argnearest__mutmut_mutants, *args, **kwargs)
    return result 

argnearest.__signature__ = _mutmut_signature(x_argnearest__mutmut_orig)
x_argnearest__mutmut_orig.__name__ = 'x_argnearest'




def x_loss_sequence__mutmut_orig(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [True, False], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_1(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=None)
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [True, False], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_2(windows_size, loss_probability, seed=None):
    random = None
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [True, False], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_3(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 2 - loss_probability
    sequence = random.choice(
        [True, False], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_4(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 + loss_probability
    sequence = random.choice(
        [True, False], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_5(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = None
    sequence = random.choice(
        [True, False], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_6(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [False, False], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_7(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [True, True], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_8(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [True, False], size=None, p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_9(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [True, False], p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_10(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [True, False], size=windows_size,
    )
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_11(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - loss_probability
    sequence = None
    if random.choice([True, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_12(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [True, False], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([False, False]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_13(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [True, False], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([True, True]):
        sequence = ~sequence
    return sequence


def x_loss_sequence__mutmut_14(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [True, False], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = sequence
    return sequence


def x_loss_sequence__mutmut_15(windows_size, loss_probability, seed=None):
    random = np.random.default_rng(seed=seed)
    probability_win = 1 - loss_probability
    sequence = random.choice(
        [True, False], size=windows_size, p=[loss_probability, probability_win]
    )
    if random.choice([True, False]):
        sequence = None
    return sequence

x_loss_sequence__mutmut_mutants = {
'x_loss_sequence__mutmut_1': x_loss_sequence__mutmut_1, 
    'x_loss_sequence__mutmut_2': x_loss_sequence__mutmut_2, 
    'x_loss_sequence__mutmut_3': x_loss_sequence__mutmut_3, 
    'x_loss_sequence__mutmut_4': x_loss_sequence__mutmut_4, 
    'x_loss_sequence__mutmut_5': x_loss_sequence__mutmut_5, 
    'x_loss_sequence__mutmut_6': x_loss_sequence__mutmut_6, 
    'x_loss_sequence__mutmut_7': x_loss_sequence__mutmut_7, 
    'x_loss_sequence__mutmut_8': x_loss_sequence__mutmut_8, 
    'x_loss_sequence__mutmut_9': x_loss_sequence__mutmut_9, 
    'x_loss_sequence__mutmut_10': x_loss_sequence__mutmut_10, 
    'x_loss_sequence__mutmut_11': x_loss_sequence__mutmut_11, 
    'x_loss_sequence__mutmut_12': x_loss_sequence__mutmut_12, 
    'x_loss_sequence__mutmut_13': x_loss_sequence__mutmut_13, 
    'x_loss_sequence__mutmut_14': x_loss_sequence__mutmut_14, 
    'x_loss_sequence__mutmut_15': x_loss_sequence__mutmut_15
}

def loss_sequence(*args, **kwargs):
    result = _mutmut_trampoline(x_loss_sequence__mutmut_orig, x_loss_sequence__mutmut_mutants, *args, **kwargs)
    return result 

loss_sequence.__signature__ = _mutmut_signature(x_loss_sequence__mutmut_orig)
x_loss_sequence__mutmut_orig.__name__ = 'x_loss_sequence'




def x_make_stock_price__mutmut_orig(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_1(price, loss, seed=None):
    if price != 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_2(price, loss, seed=None):
    if price == 1.0 :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_3(price, loss, seed=None):
    if price == 0. :
        return 1.0
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_4(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=None)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_5(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = None
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_6(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = +1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_7(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -2 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_8(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 2
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_9(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = None
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_10(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign / np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_11(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(1, 1))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_12(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 2))
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_13(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = None
    new_price = price + day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_14(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price - day_return
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_15(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = None
    return 0. if new_price < 0 else new_price


def x_make_stock_price__mutmut_16(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 1.0 if new_price < 0 else new_price


def x_make_stock_price__mutmut_17(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price <= 0 else new_price


def x_make_stock_price__mutmut_18(price, loss, seed=None):
    if price == 0. :
        return 0.
    random = np.random.default_rng(seed=seed)
    sign = -1 if loss else 1
    day_return = sign * np.abs(random.normal(0, 1))
    new_price = price + day_return
    return 0. if new_price < 1 else new_price

x_make_stock_price__mutmut_mutants = {
'x_make_stock_price__mutmut_1': x_make_stock_price__mutmut_1, 
    'x_make_stock_price__mutmut_2': x_make_stock_price__mutmut_2, 
    'x_make_stock_price__mutmut_3': x_make_stock_price__mutmut_3, 
    'x_make_stock_price__mutmut_4': x_make_stock_price__mutmut_4, 
    'x_make_stock_price__mutmut_5': x_make_stock_price__mutmut_5, 
    'x_make_stock_price__mutmut_6': x_make_stock_price__mutmut_6, 
    'x_make_stock_price__mutmut_7': x_make_stock_price__mutmut_7, 
    'x_make_stock_price__mutmut_8': x_make_stock_price__mutmut_8, 
    'x_make_stock_price__mutmut_9': x_make_stock_price__mutmut_9, 
    'x_make_stock_price__mutmut_10': x_make_stock_price__mutmut_10, 
    'x_make_stock_price__mutmut_11': x_make_stock_price__mutmut_11, 
    'x_make_stock_price__mutmut_12': x_make_stock_price__mutmut_12, 
    'x_make_stock_price__mutmut_13': x_make_stock_price__mutmut_13, 
    'x_make_stock_price__mutmut_14': x_make_stock_price__mutmut_14, 
    'x_make_stock_price__mutmut_15': x_make_stock_price__mutmut_15, 
    'x_make_stock_price__mutmut_16': x_make_stock_price__mutmut_16, 
    'x_make_stock_price__mutmut_17': x_make_stock_price__mutmut_17, 
    'x_make_stock_price__mutmut_18': x_make_stock_price__mutmut_18
}

def make_stock_price(*args, **kwargs):
    result = _mutmut_trampoline(x_make_stock_price__mutmut_orig, x_make_stock_price__mutmut_mutants, *args, **kwargs)
    return result 

make_stock_price.__signature__ = _mutmut_signature(x_make_stock_price__mutmut_orig)
x_make_stock_price__mutmut_orig.__name__ = 'x_make_stock_price'



