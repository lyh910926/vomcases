arguments:
- position: 18
  separate: true
  shellQuote: true
  valueFrom: --legend
- position: 27
  separate: true
  shellQuote: true
  valueFrom: --xloc_title
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/plot_timeseries.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default:
      class: File
      path: ../../data/DINGO_QC/FeQ_daly.txt
    inputBinding:
      position: 10
      prefix: --eobs_qc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/DINGO/Ea_daly.txt
    inputBinding:
      position: 11
      prefix: --eobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default: red
    inputBinding:
      position: 12
      prefix: --colors
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_13:
    default: black
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_14:
    default:
      class: File
      path: ../../data/fPAR/fpar_daly_v5.txt
    inputBinding:
      position: 14
      prefix: --pcobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_15:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 15
      prefix: --pcobsdates
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default: predicted cover
    inputBinding:
      position: 16
      prefix: --labels
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_17:
    default: prescribed cover
    inputBinding:
      position: 17
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_19:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 19
      prefix: --stats_evap
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_20:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 21
      prefix: --stats_ass
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_22:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 22
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/pc_beststats.txt
    inputBinding:
      position: 23
      prefix: --stats_pc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_24:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/pc_beststats.txt
    inputBinding:
      position: 24
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default: MAE predicted
    inputBinding:
      position: 25
      prefix: --stats_label
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_26:
    default: MAE prescribed
    inputBinding:
      position: 26
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_28:
    default: '.10'
    inputBinding:
      position: 28
      prefix: '-0'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_29:
    default: '1.10'
    inputBinding:
      position: 29
      prefix: --yloc_title
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_best/results_daily.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_30:
    default: 24
    inputBinding:
      position: 30
      prefix: --size_title
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_31:
    default: 7
    inputBinding:
      position: 31
      prefix: --moving_average
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_32:
    default: evaptot
    inputBinding:
      position: 32
      prefix: --var
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_33:
    default: asstot
    inputBinding:
      position: 33
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_34:
    default: pc
    inputBinding:
      position: 34
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_35:
    default: 10
    inputBinding:
      position: 35
      prefix: --ymax
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_36:
    default: '1.5'
    inputBinding:
      position: 36
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_37:
    default: 100
    inputBinding:
      position: 37
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_38:
    default: 0
    inputBinding:
      position: 38
      prefix: --ymin
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_39:
    default: 0
    inputBinding:
      position: 39
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_4:
    default: s
    inputBinding:
      position: 4
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_40:
    default: 0
    inputBinding:
      position: 40
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_41:
    default: 16
    inputBinding:
      position: 41
      prefix: --figsize
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_42:
    default: 15
    inputBinding:
      position: 42
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_43:
    default: data/img/9_pc_daly.png
    inputBinding:
      position: 43
      prefix: --outputfile
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: 2008
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_6:
    default: e
    inputBinding:
      position: 6
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default: 2012
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_8:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_daly.txt
    inputBinding:
      position: 8
      prefix: --assobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../data/DINGO_QC/FcQ_daly.txt
    inputBinding:
      position: 9
      prefix: --assobs_qc
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_43)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/img
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/plot_timeseries.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/DINGO/GPPdaily_daly.txt
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/DINGO_QC/FcQ_daly.txt
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/DINGO_QC/FeQ_daly.txt
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/DINGO/Ea_daly.txt
    writable: false
  - entry: $(inputs.input_14)
    entryname: data/fPAR/fpar_daly_v5.txt
    writable: false
  - entry: $(inputs.input_15)
    entryname: data/fPAR/dates_v5
    writable: false
  - entry: $(inputs.input_19)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_20)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_21)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_22)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_23)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/pc_beststats.txt
    writable: false
  - entry: $(inputs.input_24)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/pc_beststats.txt
    writable: false
successCodes: []
temporaryFailCodes: []
