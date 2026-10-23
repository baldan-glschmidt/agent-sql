# R144INS

## Descrição

BS - Instituições Outra Empresa

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodOem | Number(008,0) | Não | Código da Outra Empresa |
| CodTip | Number(003,0) | Não | Tipo Instituição |
| CodSer | Number(003,0) | Não | Código do Serviço |
| ValSer | Number(008,2) | Sim | Valor do Serviço |

---

## Chave Primária

- CodOem
- CodTip
- CodSer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R144INS_000

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

### IR_R144INS_001

**Tabela:** R144TIP

| Origem | Destino |
|--------|---------|
| CodTip | CodTip |

### IR_R144INS_002

**Tabela:** R144SER

| Origem | Destino |
|--------|---------|
| CodSer | CodSer |

