# E000CHE

## Descrição

Tabelas - Integrações - Preparação de Tesouraria (Cheques/Avisos)

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| NumCco | String(014) | Não | Número da conta interna |
| OriChe | String(002) | Não | Origem da solicitação de emissão de cheque ou aviso de débito |
| DatPre | Date | Não | Data prevista de emissão do cheque ou aviso de débito |
| DatLib | Date | Não | Data da liberação do cheque ou aviso de débito |
| SeqChe | String(006) | Não | Sequência de cheque ou aviso de débito - agrupamento |
| IdeUni | String(050) | Sim | Identificador único alfanumérico |

---

## Chave Primária

- SeqInt

---

## Índices

### E000CHEIndice1

**Tipo:** Unico

Campos:
- CodEmp
- NumCco
- OriChe
- DatPre
- DatLib
- SeqChe

---

## Relacionamentos

Nenhum relacionamento cadastrado.
