# R098EQI

## Descrição

Equipamentos - Anexos

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipEqp | Number(003,0) | Não | Código Tipo de Equipamento |
| CodEqp | Number(006,0) | Não | Código do Equipamento |
| SeqImg | Number(003,0) | Não | Sequência do Anexo |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| DesImg | String(030) | Sim | Descrição do Anexo |
| Imagem | Image | Sim | Anexo |

---

## Chave Primária

- NumEmp
- TipEqp
- CodEqp
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R098EQI_001

**Tabela:** R098TEQ

| Origem | Destino |
|--------|---------|
| TipEqp | TipEqp |

### IR_R098EQI_002

**Tabela:** R098EQP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipEqp | TipEqp |
| CodEqp | CodEqp |

