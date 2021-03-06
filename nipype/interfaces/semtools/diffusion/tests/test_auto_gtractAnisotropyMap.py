# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..gtract import gtractAnisotropyMap


def test_gtractAnisotropyMap_inputs():
    input_map = dict(
        anisotropyType=dict(argstr="--anisotropyType %s",),
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        inputTensorVolume=dict(argstr="--inputTensorVolume %s", extensions=None,),
        numberOfThreads=dict(argstr="--numberOfThreads %d",),
        outputVolume=dict(argstr="--outputVolume %s", hash_files=False,),
    )
    inputs = gtractAnisotropyMap.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_gtractAnisotropyMap_outputs():
    output_map = dict(outputVolume=dict(extensions=None,),)
    outputs = gtractAnisotropyMap.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
