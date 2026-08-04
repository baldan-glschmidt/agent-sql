# E000SAC

## Descrição

Tabelas - Integrações - Sacado

---

## Resumo

- Campos: 6
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
| CodSac | Number(014,0) | Não | Número do CNPJ ou CPF do sacado |
| IdeSac | String(050) | Sim | Identificador único alfanumérico |
| DocIdeSac | String(014) | Sim | Número do CNPJ ou CPF do sacado |

---

## Chave Primária

- SeqInt

---

## Índices

### E000SACIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodSac
- DocIdeSac

---

## Relacionamentos

Nenhum relacionamento cadastrado.
