# E044BLO

## Descrição

Tabelas - Bloqueio de Movimento de Estoque

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFam | String(006) | Sim | Código da família de Produtos |
| DatIni | Date | Não | Data Inicial do Movimento |
| DatFim | Date | Não | Data Final do Movimento |
| ObsBlo | String(250) | Sim | Observação do Bloqueio |
| LibBlo | String(001) | Sim | Opção de Bloqueio |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E044BLOIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFam
- DatIni
- DatFim

---

## Relacionamentos

Nenhum relacionamento cadastrado.
