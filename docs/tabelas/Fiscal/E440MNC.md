# E440MNC

## Descrição

Compras - Notas Fiscais de Entrada - Mensagens

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqMnc | Number(009,0) | Não | Sequência da mensagem |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| CodMsg | Number(004,0) | Não | Código da mensagem da nota fiscal de entrada |
| MsgNfc | String(1000) | Não | Texto da mensagem da nota fiscal de entrada |

---

## Chave Primária

- SeqMnc

---

## Índices

### E440MNCNotaEntrada

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf

---

## Relacionamentos

### IR_E440MNC_003

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E440MNC_005

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

