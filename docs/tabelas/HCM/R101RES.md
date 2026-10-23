# R101RES

## Descrição

Avaliação de Resultado - Objetivos - Notas

---

## Resumo

- Campos: 41
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Não | Sequência do tipo de avaliação |
| SeqAva | Number(002,0) | Não | Sequência da avaliação |
| IdeObj | Number(006,0) | Não | Identificação dos objetivos |
| DesObj | String(2000) | Sim | Descrição do objetivo |
| SeqObj | Number(006,0) | Sim | Sequência do objetivo |
| PriObj | Number(003,0) | Sim | Prioridade do objetivo |
| PesObj | Number(005,2) | Sim | Peso do objetivo |
| TipRes | Number(001,0) | Sim | Tipo do resultado |
| NotObj | Number(016,4) | Sim | Resultado da avaliação de objetivos |
| ApuRes | Number(001,0) | Sim | Apuração do objetivo |
| PerObj | Number(014,2) | Sim | % atingido na avaliação dos objetivos |
| VlrSt1 | Number(016,4) | Sim | Valor do step mínimo |
| VlrSt2 | Number(016,4) | Sim | Valor do step target |
| VlrSt3 | Number(016,4) | Sim | Valor do step máximo |
| DirObj | Number(001,0) | Sim | Direção para avaliação do objetivo |
| DesInd | String(300) | Sim | Descrição de orientação do indicador |
| DesMet | String(300) | Sim | Descrição de orientação das metas |
| DesRes | String(2000) | Sim | Descrição do resultado |
| ComChe | String(1500) | Sim | Comentário do avaliador que justifica a nota |
| ComEmp | String(1500) | Sim | Comentário do avaliado |
| OriObj | Number(001,0) | Sim | Identificação da origem do objetivo |
| CodCla | Number(004,0) | Sim | Código da classe dos objetivos |
| CodBlo | Number(004,0) | Sim | Código do bloco da classe dos objetivos |
| NotChe | Number(016,4) | Sim | Resultado da avaliação de objetivos - Nota do Avaliador |
| SitObj | Number(001,0) | Sim | Situação do Objetivo |
| LimMin | Number(005,2) | Sim | Limite mínimo para ser considerado na apuração do resultado |
| LimMax | Number(005,2) | Sim | Limite máximo para ser considerado na apuração do resultado |
| CodTpr | Number(004,0) | Sim | Tabela de proficiências da evidência da competência |
| CodCPr | String(010) | Sim | Conceito avaliado para a evidência da competência |
| TipOar | Number(001,0) | Sim | Tipo do objetivo da avaliação de resultados |
| EmpObC | Number(004,0) | Sim | Código da Empresa |
| TipObC | Number(001,0) | Sim | Tipo Colaborador |
| CadObC | Number(009,0) | Sim | Código do Colaborador |
| CicObC | Number(003,0) | Sim | Código do ciclo de avaliação |
| TAvObC | Number(002,0) | Sim | Sequência do tipo de avaliação |
| SeqObC | Number(002,0) | Sim | Sequência |
| IdeObC | Number(006,0) | Sim | Identificação do objetivo coletivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- TipAva
- SeqAva
- IdeObj

---

## Índices

### R101RESIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodCic
- TipAva
- SeqAva
- IdeObj
- SeqObj

---

## Relacionamentos

### IR_R101RES_005

**Tabela:** R101AVA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| TipAva | TipAva |
| SeqAva | SeqAva |

