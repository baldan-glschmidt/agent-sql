# R351IVC

## Descrição

S-2500 - eSocial - Informações dos vínculos/contratos incorporados, no caso de reconhecimento de unicidade contratual

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CpfTra | Number(011,0) | Não | Número do CPF do trabalhador |
| IdeSeq | Number(005,0) | Não | Sequência parcial |
| SeqPtb | Number(009,0) | Não | Sequência |
| SeqIct | Number(009,0) | Não | Sequência |
| SeqIvc | Number(009,0) | Não | Sequência |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| MatInc | String(030) | Sim | Matrícula cujo vínculo/contrato passou a integrar período de unicidade contratual reconhecido judicialmente |
| CodCat | Number(004,0) | Sim | Código da categoria cujo contrato passou a integrar período de unicidade contratual reconhecido judicialmente |
| DatIni | Date | Sim | Data de início de TSVE cujo contrato passou a integrar período de unicidade contratual reconhecido judicialmente |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- CpfTra
- IdeSeq
- SeqPtb
- SeqIct
- SeqIvc

---

## Índices

### R351IVCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
