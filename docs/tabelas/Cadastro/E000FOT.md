# E000FOT

## Descrição

Tabelas - Integrações - Filiais de Operadoras de Telefonia

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodOte | Number(004,0) | Não | Código da operadora de telefonia |
| CodFot | Number(003,0) | Não | Sequencia da filial de operadora de telefonia |

---

## Chave Primária

- SeqInt

---

## Índices

### E000FOTIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodOte
- CodFot

---

## Relacionamentos

Nenhum relacionamento cadastrado.
