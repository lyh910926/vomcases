arguments:
- position: 28
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
      path: ../../src_py/plot_et_ass_pc.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default:
      class: File
      path: ../../data/DINGO_QC/FcQ_daly.txt
    inputBinding:
      position: 10
      prefix: --assobs_qc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/DINGO_QC/FeQ_daly.txt
    inputBinding:
      position: 11
      prefix: --eobs_qc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../data/DINGO/Ea_daly.txt
    inputBinding:
      position: 12
      prefix: --eobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default: red
    inputBinding:
      position: 13
      prefix: --colors
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_14:
    default: black
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_15:
    default:
      class: File
      path: ../../data/fPAR/fpar_daly_v5.txt
    inputBinding:
      position: 15
      prefix: --pcobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 16
      prefix: --pcobsdates
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_17:
    default: predicted cover
    inputBinding:
      position: 17
      prefix: --labels
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_18:
    default: prescribed cover
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_19:
    default: 'True'
    inputBinding:
      position: 19
      prefix: --legend
      separate: true
      shellQuote: true
    streamable: false
    type: string
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
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 20
      prefix: --stats_evap
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 21
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_22:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 22
      prefix: --stats_ass
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 23
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_24:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/pc_beststats.txt
    inputBinding:
      position: 24
      prefix: --stats_pc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/pc_beststats.txt
    inputBinding:
      position: 25
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default: MAE predicted
    inputBinding:
      position: 26
      prefix: --stats_label
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_27:
    default: MAE prescribed
    inputBinding:
      position: 27
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_29:
    default: '.05'
    inputBinding:
      position: 29
      prefix: '-0'
      separate: false
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
    default: '1.10'
    inputBinding:
      position: 30
      prefix: --yloc_title
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_31:
    default: 24
    inputBinding:
      position: 31
      prefix: --size_title
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_32:
    default: 7
    inputBinding:
      position: 32
      prefix: --moving_average
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_33:
    default: data/img/9_pc_daly.png
    inputBinding:
      position: 33
      prefix: --outputfile
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default: s
    inputBinding:
      position: 4
      prefix: -y
      separate: false
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
      path: ../../data/VOM_input/DalyUncleared/dailyweather.prn
    inputBinding:
      position: 8
      prefix: -w
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_daly.txt
    inputBinding:
      position: 9
      prefix: --assobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_33)
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
    entryname: src_py/plot_et_ass_pc.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/VOM_input/DalyUncleared/dailyweather.prn
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/DINGO/GPPdaily_daly.txt
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/DINGO_QC/FcQ_daly.txt
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/DINGO_QC/FeQ_daly.txt
    writable: false
  - entry: $(inputs.input_12)
    entryname: data/DINGO/Ea_daly.txt
    writable: false
  - entry: $(inputs.input_15)
    entryname: data/fPAR/fpar_daly_v5.txt
    writable: false
  - entry: $(inputs.input_16)
    entryname: data/fPAR/dates_v5
    writable: false
  - entry: $(inputs.input_20)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_21)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_22)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_23)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_24)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/pc_beststats.txt
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/pc_beststats.txt
    writable: false
successCodes: []
temporaryFailCodes: []
