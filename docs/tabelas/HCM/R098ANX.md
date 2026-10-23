# R098ANX

## Descrição

Revisão Equipamentos - Anexos

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipEqp | Number(003,0) | Não | Código Tipo de Equipamento |
| CodEqp | Number(006,0) | Não | Código do Equipamento |
| TipSvc | Number(003,0) | Não | Código Tipo de Serviço |
| DatRev | Date | Não | Data da Revisão |
| SeqAne | Number(002,0) | Não | Sequência do anexo |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| DesAne | String(060) | Sim | Descrição do arquivo anexo |
| ArqAne | Image | Sim | Arquivo anexo |

---

## Chave Primária

- NumEmp
- TipEqp
- CodEqp
- TipSvc
- DatRev
- SeqAne

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R098ANX_004

**Tabela:** R098REV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipEqp | TipEqp |
| CodEqp | CodEqp |
| TipSvc | TipSvc |
| DatRev | DatRev |

