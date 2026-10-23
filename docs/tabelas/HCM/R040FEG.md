# R040FEG

## Descrição

Recibo de Férias - Afastamentos

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| IniPer | Date | Não | Início do Período Aquisitivo |
| IniFer | Date | Não | Início das Férias |
| SeqAfa | Number(002,0) | Não | Sequência do Afastamento |
| IniAfa | Date | Sim | Início do Afastamento de Férias |
| TerAfa | Date | Sim | Término do Afastamento de Férias |
| DiaAfa | Number(004,2) | Sim | Quantidade de Dias Afastamento |
| ObsAfa | String(040) | Sim | Observação do Afastamento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniPer
- IniFer
- SeqAfa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R040FEG_003

**Tabela:** R040PER

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| IniPer | IniPer |

### IR_R040FEG_004

**Tabela:** R040FEM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| IniPer | IniPer |
| IniFer | IniFer |

