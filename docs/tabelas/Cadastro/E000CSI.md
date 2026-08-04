# E000CSI

## Descrição

Tabelas - Integração - Cadastro de serviços intermediados

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| IdeCsi | Number(009,0) | Não | Identificador de registro |

---

## Chave Primária

- SeqInt

---

## Índices

### E000CSIIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- IdeCsi

### E000CSIIndice2

**Tipo:** Não unico

Campos:
- IdeCsi

---

## Relacionamentos

### IR_E000CSI_003

**Tabela:** E080CSI

| Origem | Destino |
|--------|---------|
| IdeCsi | IdeUni |

