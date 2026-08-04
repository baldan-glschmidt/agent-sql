# E050PAC

## Descrição

Tabelas - Tributos - Controle de produção de usina

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| RegEfd | Number(002,0) | Sim | Identificador do campo referente ao registro 1391 do SPED Fiscal |
| ClaAlc | Number(002,0) | Sim | Classificação do produto para a produção de açúcar e álcool |
| UniMed | String(003) | Sim | Unidade de medida utilizada nos registros das declarações |
| ValIni | Date | Não | Validade inicial |
| ValFim | Date | Não | Validade final |
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

### E050PACIndex1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- RegEfd
- ClaAlc
- ValIni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
