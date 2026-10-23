# R070LFH

## Descrição

Liberação da Faixa Horária

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCra | Number(012,0) | Não | Número do Crachá |
| DatLib | Date | Não | Data de Liberação |
| HorIni | Number(005,0) | Não | Hora Inicio da Liberação da Faixa Horária |
| HorFim | Number(005,0) | Sim | Hora Final da Liberação da Faixa Horária |
| ObsLib | String(080) | Sim | Observação da Liberação |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Bloqueou/Liberou o Crachá |

---

## Chave Primária

- NumCra
- DatLib
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
