# E000TPS

## Descrição

Tabelas - Integrações - Tributos de Serviço no Documento Fiscal

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
| CodEmp | Number(004,0) | Sim | Código da empresa |
| CodFil | Number(005,0) | Sim | Código da filial |
| CodSer | String(014) | Sim | Código do serviço |
| PerInf | Date | Sim | Data base inicial de validade |

---

## Chave Primária

- SeqInt

---

## Índices

### E000TPSIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodSer
- PerInf

---

## Relacionamentos

Nenhum relacionamento cadastrado.
