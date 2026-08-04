# E070PRF

## Descrição

Cadastros - Empresa - Tributos - Período do Refis

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqPer | Number(009,0) | Não | Sequência do registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| PerIni | Date | Não | Período inicial do Refis |
| PerFim | Date | Não | Período final do Refis |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- SeqPer

---

## Índices

### E070PRFIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- PerIni
- PerFim

---

## Relacionamentos

Nenhum relacionamento cadastrado.
