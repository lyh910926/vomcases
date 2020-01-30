arguments:
- position: 39
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
      path: ../../data/DINGO/GPPdaily_daly.txt
    inputBinding:
      position: 10
      prefix: --assobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/DINGO_QC/FcQ_daly.txt
    inputBinding:
      position: 11
      prefix: --assobs_qc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../data/DINGO_QC/FeQ_daly.txt
    inputBinding:
      position: 12
      prefix: --eobs_qc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default:
      class: File
      path: ../../data/DINGO/Ea_daly.txt
    inputBinding:
      position: 13
      prefix: --eobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_14:
    default: red
    inputBinding:
      position: 14
      prefix: --colors
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_15:
    default: black
    inputBinding:
      position: 15
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_16:
    default: green
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_17:
    default:
      class: File
      path: ../../data/fPAR/fpar_daly_v5.txt
    inputBinding:
      position: 17
      prefix: --pcobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_18:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 18
      prefix: --pcobsdates
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_19:
    default: predicted cover
    inputBinding:
      position: 19
      prefix: --labels
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
    default: prescribed cover
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_21:
    default: prescribed cover
    inputBinding:
      position: 21
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_22:
    default: mean
    inputBinding:
      position: 22
      prefix: '-'
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_23:
    default: monthly
    inputBinding:
      position: 23
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_24:
    default: 'True'
    inputBinding:
      position: 24
      prefix: --legend
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_25:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 25
      prefix: --stats_evap
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 26
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_27:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/DalyUncleared/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 27
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_28:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 28
      prefix: --stats_ass
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_29:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 29
      separate: true
      shellQuote: true
    streamable: false
    type: File
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
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/DalyUncleared/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_31:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/pc_beststats.txt
    inputBinding:
      position: 31
      prefix: --stats_pc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_32:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/pc_beststats.txt
    inputBinding:
      position: 32
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_33:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/DalyUncleared/sce_stats_best/pc_beststats.txt
    inputBinding:
      position: 33
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_34:
    default: MAE predicted
    inputBinding:
      position: 34
      prefix: --stats_label
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_35:
    default: MAE prescribed
    inputBinding:
      position: 35
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_36:
    default: MAE prescribed
    inputBinding:
      position: 36
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_37:
    default: mean
    inputBinding:
      position: 37
      prefix: '-'
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_38:
    default: monthly
    inputBinding:
      position: 38
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover2/DalyUncleared/sce_best/results_daily.txt
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_40:
    default: '.05'
    inputBinding:
      position: 40
      prefix: '-0'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_41:
    default: '1.10'
    inputBinding:
      position: 41
      prefix: --yloc_title
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_42:
    default: 24
    inputBinding:
      position: 42
      prefix: --size_title
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
    default: s
    inputBinding:
      position: 5
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default: 2008
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_7:
    default: e
    inputBinding:
      position: 7
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_8:
    default: 2012
    inputBinding:
      position: 8
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_9:
    default:
      class: File
      path: ../../data/VOM_input/DalyUncleared/dailyweather.prn
    inputBinding:
      position: 9
      prefix: -w
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
    entryname: src_py/plot_et_ass_pc.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/DalyUncleared/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/VOM_input/DalyUncleared/dailyweather.prn
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/DINGO/GPPdaily_daly.txt
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/DINGO_QC/FcQ_daly.txt
    writable: false
  - entry: $(inputs.input_12)
    entryname: data/DINGO_QC/FeQ_daly.txt
    writable: false
  - entry: $(inputs.input_13)
    entryname: data/DINGO/Ea_daly.txt
    writable: false
  - entry: $(inputs.input_17)
    entryname: data/fPAR/fpar_daly_v5.txt
    writable: false
  - entry: $(inputs.input_18)
    entryname: data/fPAR/dates_v5
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_26)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_27)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/DalyUncleared/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_28)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_29)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_30)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/DalyUncleared/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_31)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best/pc_beststats.txt
    writable: false
  - entry: $(inputs.input_32)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_stats_best/pc_beststats.txt
    writable: false
  - entry: $(inputs.input_33)
    entryname: data/VOM_output/additional_analyses/prescribed_cover2/DalyUncleared/sce_stats_best/pc_beststats.txt
    writable: false
successCodes: []
temporaryFailCodes: []
