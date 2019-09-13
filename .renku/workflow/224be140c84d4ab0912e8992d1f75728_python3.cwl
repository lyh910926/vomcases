arguments: []
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/proc_sce_pc_restart.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default:
      class: File
      path: ../../work/additional_analyses/prescribed_cover/DryRiver/input/perc_cov.txt
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default: 10
    inputBinding:
      position: 11
      prefix: -p
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_12:
    default: p
    inputBinding:
      position: 12
      prefix: -o
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_13:
    default: 1
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_14:
    default: 1
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_15:
    default: 1
    inputBinding:
      position: 15
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_16:
    default: 1
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_17:
    default: 1
    inputBinding:
      position: 17
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_18:
    default: 1
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_19:
    default: 0
    inputBinding:
      position: 19
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce/sce_out.txt
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_20:
    default: 1
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_21:
    default: o
    inputBinding:
      position: 21
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_22:
    default:
      class: File
      path: ../../data/DINGO/Ea_dry.txt
    inputBinding:
      position: 22
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default: o
    inputBinding:
      position: 23
      prefix: -a
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_24:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_dry.txt
    inputBinding:
      position: 24
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default: d
    inputBinding:
      position: 25
      prefix: -c
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_26:
    default:
      class: Directory
      listing: []
      path: ../../src/VOM/VOM_Fortran
    inputBinding:
      position: 26
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_27:
    default: d
    inputBinding:
      position: 27
      prefix: -s
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_28:
    default: 01-01-1980
    inputBinding:
      position: 28
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_29:
    default: d
    inputBinding:
      position: 29
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default: data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce_stats2
    inputBinding:
      position: 3
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_30:
    default: 21-12-2016
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_31:
    default:
      class: Directory
      listing: []
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce_stats
    inputBinding:
      position: 31
      prefix: --restartdir
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_32:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/coreprog.f90
    inputBinding:
      position: 32
      prefix: -c
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_33:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/modules.f90
    inputBinding:
      position: 33
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_34:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/readdata.f90
    inputBinding:
      position: 34
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_35:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/sample.f90
    inputBinding:
      position: 35
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_36:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/sce.f90
    inputBinding:
      position: 36
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_37:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/transpmodel.f90
    inputBinding:
      position: 37
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_38:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/watbal.f90
    inputBinding:
      position: 38
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default: b
    inputBinding:
      position: 4
      prefix: -o
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce_best
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default:
      class: File
      path: ../../work/additional_analyses/prescribed_cover/DryRiver/best/vom_namelist
    inputBinding:
      position: 6
      prefix: -n
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default:
      class: Directory
      listing: []
      path: ../../work/additional_analyses/prescribed_cover/DryRiver/best
    inputBinding:
      position: 7
      prefix: -w
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_8:
    default:
      class: File
      path: ../../work/additional_analyses/prescribed_cover/DryRiver/input/dailyweather.prn
    inputBinding:
      position: 8
      prefix: -d
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default: c
    inputBinding:
      position: 9
      prefix: -p
      separate: false
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_3)
    streamable: false
    type: Directory
  output_1:
    outputBinding:
      glob: $(inputs.input_5)
    streamable: false
    type: Directory
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce_best
    writable: true
successCodes: []
temporaryFailCodes: []
