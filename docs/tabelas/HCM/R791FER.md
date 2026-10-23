# R791FER

## Descrição

Central alertas - Férias - Vencimento 2 Período

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| IniPer | Date | Não | Início do Período aquisitivo de férias |
| FimPer | Date | Não | Fim do Período aquisitivo de férias |
| QtdSld | Number(005,2) | Não | Saldo de dias de férias no período aquisitivo |
| DiaRes | Number(004,0) | Não | Dias até o limite concessivo de ferias |
| InsLev | Number(001,0) | Não | Nível de severidade da ocorrência |
| DatGer | Date | Não | Data de geração do registro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniPer

---

## Índices

### R791FERIndice1

**Tipo:** Não unico

Campos:
- InsLev

---

## Relacionamentos

Nenhum relacionamento cadastrado.
