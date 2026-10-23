# R164AIP

## Descrição

Histórico de informações do plano - Anexos

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodOem | Number(008,0) | Não | Código Outra Empresa |
| CodPla | Number(003,0) | Não | Código do Plano |
| DatAlt | Date | Não | Data da alteração do histórico |
| TipAca | String(001) | Não | Indica se é inclusão, alteração ou exclusão no plano |
| SeqAne | Number(002,0) | Não | Sequência do anexo |
| DesArq | String(250) | Sim | Descrição do arquivo anexado |
| NomArq | String(250) | Sim | Nome do arquivo anexado |
| DocAne | Image | Sim | Arquivo anexo |

---

## Chave Primária

- CodOem
- CodPla
- DatAlt
- TipAca
- SeqAne

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R164AIP_000

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

### IR_R164AIP_001

**Tabela:** R164PLA

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |
| CodPla | CodPla |

### IR_R164AIP_003

**Tabela:** R164HAP

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |
| CodPla | CodPla |
| DatAlt | DatAlt |
| TipAca | TipAca |

