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
      path: ../../src_py/dingo_dailyweather.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default:
      class: File
      path: ../../data/DINGO2/Fsd_howard.txt
    inputBinding:
      position: 10
      prefix: --radnfile
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/DINGO2/VP_howard.txt
    inputBinding:
      position: 11
      prefix: --vpfile
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../data/DINGO2/Pres_howard.txt
    inputBinding:
      position: 12
      prefix: --presfile
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default: m
    inputBinding:
      position: 2
      prefix: -i
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default:
      class: File
      path: ../../data/Silo/howard.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default: c
    inputBinding:
      position: 4
      prefix: -i
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default:
      class: File
      path: ../../data/MaunaLoa/weekly_in_situ_co2_mlo.csv
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default: work/additional_analyses/sens_weatherdata/2_dingo_sce/input/dailyweather.prn
    inputBinding:
      position: 6
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default:
      class: File
      path: ../../data/DINGO2/Tmax_howard.txt
    inputBinding:
      position: 7
      prefix: --tmaxfile
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default:
      class: File
      path: ../../data/DINGO2/Tmin_howard.txt
    inputBinding:
      position: 8
      prefix: --tminfile
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../data/DINGO2/Prec_howard.txt
    inputBinding:
      position: 9
      prefix: --rainfile
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_6)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: work/additional_analyses/sens_weatherdata/2_dingo_sce/input
    writable: true
successCodes: []
temporaryFailCodes: []
