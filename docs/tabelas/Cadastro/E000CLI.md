# E000CLI

## Descrição

Tabelas - Integrações - Clientes

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodCli | Number(009,0) | Não | Código do cliente |

---

## Chave Primária

- SeqInt

---

## Índices

### E000CLIIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodCli

### E000CLIEmpresaFilial

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

Nenhum relacionamento cadastrado.
