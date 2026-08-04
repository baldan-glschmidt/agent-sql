# E000TPD

## Descrição

Tabelas - Integrações - Tributos de Produto no Documento Fiscal

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
| CodEmp | Number(004,0) | Sim | Código da empresa |
| CodFil | Number(005,0) | Sim | Código da filial |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| PerInf | Date | Sim | Data base inicial de validade |

---

## Chave Primária

- SeqInt

---

## Índices

### E000TPDIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodPro
- CodDer
- PerInf

---

## Relacionamentos

Nenhum relacionamento cadastrado.
