arguments:
- position: 36
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
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.8/sce_best/results_daily.txt
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff2.0/sce_best/results_daily.txt
    inputBinding:
      position: 11
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff2.2/sce_best/results_daily.txt
    inputBinding:
      position: 12
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff2.4/sce_best/results_daily.txt
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_14:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff2.6/sce_best/results_daily.txt
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_15:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff2.8/sce_best/results_daily.txt
    inputBinding:
      position: 15
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff3.0/sce_best/results_daily.txt
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_17:
    default: s
    inputBinding:
      position: 17
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_18:
    default: 2006
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_19:
    default: e
    inputBinding:
      position: 19
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff0.2/sce_best/results_daily.txt
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_20:
    default: 2010
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_21:
    default:
      class: File
      path: ../../data/VOM_input/HowardSprings/dailyweather.prn
    inputBinding:
      position: 21
      prefix: -w
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_22:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_howard.txt
    inputBinding:
      position: 22
      prefix: --assobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default:
      class: File
      path: ../../data/DINGO_QC/FcQ_howard.txt
    inputBinding:
      position: 23
      prefix: --assobs_qc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_24:
    default:
      class: File
      path: ../../data/DINGO_QC/FeQ_howard.txt
    inputBinding:
      position: 24
      prefix: --eobs_qc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default:
      class: File
      path: ../../data/DINGO/Ea_howard.txt
    inputBinding:
      position: 25
      prefix: --eobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default:
      class: File
      path: ../../data/fPAR/fpar_howard_v5.txt
    inputBinding:
      position: 26
      prefix: --pcobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_27:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 27
      prefix: --pcobsdates
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_28:
    default: prescribed
    inputBinding:
      position: 28
      prefix: --labels
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_29:
    default: cover
    inputBinding:
      position: 29
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff0.4/sce_best/results_daily.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_30:
    default: predicted
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_31:
    default: cover
    inputBinding:
      position: 31
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_32:
    default: 'True'
    inputBinding:
      position: 32
      prefix: --legend
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_33:
    default: 'True'
    inputBinding:
      position: 33
      prefix: --plot_cbar
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_34:
    default: $c_{cpccf}$ ($\mu mol m^3 s^{-1})$
    inputBinding:
      position: 34
      prefix: --cblabel
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_35:
    default: '3.0'
    inputBinding:
      position: 35
      prefix: --cbar_max
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_37:
    default: '.05'
    inputBinding:
      position: 37
      prefix: '-0'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_38:
    default: '1.10'
    inputBinding:
      position: 38
      prefix: --yloc_title
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_39:
    default: 24
    inputBinding:
      position: 39
      prefix: --size_title
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_4:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff0.6/sce_best/results_daily.txt
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_40:
    default: RdYlGn
    inputBinding:
      position: 40
      prefix: --palette
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_41:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 41
      prefix: --stats_evap
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_42:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff0.6/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 42
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_43:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 43
      prefix: --stats_ass
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_44:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff0.6/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 44
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_45:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/pc_beststats.txt
    inputBinding:
      position: 45
      prefix: --stats_pc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_46:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff0.6/sce_stats_best/pc_beststats.txt
    inputBinding:
      position: 46
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_47:
    default:
    - MAE c$_{cpccf
    - 1.0}$
    inputBinding:
      itemSeparator: ','
      position: 47
      prefix: --stats_label
      separate: true
      shellQuote: true
    streamable: false
    type: string[]
  input_48:
    default:
    - MAE c$_{cpccf
    - 0.6}$
    inputBinding:
      itemSeparator: ','
      position: 48
      separate: true
      shellQuote: true
    streamable: false
    type: string[]
  input_49:
    default: data/img/5_hs_fluxes.png
    inputBinding:
      position: 49
      prefix: --outputfile
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff0.8/sce_best/results_daily.txt
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.2/sce_best/results_daily.txt
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.4/sce_best/results_daily.txt
    inputBinding:
      position: 8
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.6/sce_best/results_daily.txt
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_49)
    streamable: false
    type: File
  output_1:
    outputBinding:
      glob: notebooks/results.ipynb
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: notebooks
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/img
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/plot_et_ass_pc.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff0.2/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff0.4/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff0.6/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_5)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff0.8/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_6)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_7)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.2/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.4/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.6/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.8/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff2.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_12)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff2.2/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_13)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff2.4/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_14)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff2.6/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_15)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff2.8/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_16)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff3.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_21)
    entryname: data/VOM_input/HowardSprings/dailyweather.prn
    writable: false
  - entry: $(inputs.input_22)
    entryname: data/DINGO/GPPdaily_howard.txt
    writable: false
  - entry: $(inputs.input_23)
    entryname: data/DINGO_QC/FcQ_howard.txt
    writable: false
  - entry: $(inputs.input_24)
    entryname: data/DINGO_QC/FeQ_howard.txt
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/DINGO/Ea_howard.txt
    writable: false
  - entry: $(inputs.input_26)
    entryname: data/fPAR/fpar_howard_v5.txt
    writable: false
  - entry: $(inputs.input_27)
    entryname: data/fPAR/dates_v5
    writable: false
  - entry: $(inputs.input_41)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_42)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff0.6/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_43)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_44)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff0.6/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_45)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/pc_beststats.txt
    writable: false
  - entry: $(inputs.input_46)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff0.6/sce_stats_best/pc_beststats.txt
    writable: false
successCodes: []
temporaryFailCodes: []
