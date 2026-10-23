# R038AAF

## Descrição

Afastamentos - Acompanhamento

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAfa | Date | Não | Data do Afastamento |
| HorAfa | Number(005,0) | Não | Hora do Afastamento |
| DatAco | Date | Não | Data do Acompanhamento |
| DatPrx | Date | Sim | Data do Próximo Acompanhamento |
| ObsAco | String(500) | Sim | Observações do Acompanhamento |
| CodRec | Number(002,0) | Sim | Sequência do recurso |
| DatDec | Date | Sim | Data da Decisão do Recurso |
| ResRec | Number(001,0) | Sim | Resultado do recurso (Favorável / Contrário) |
| PrxRec | Number(001,0) | Sim | Indica se haverá novo recurso |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAfa
- HorAfa
- DatAco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038AAF_004

**Tabela:** R038AFA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatAfa | DatAfa |
| HorAfa | HorAfa |

