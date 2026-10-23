# R158PES

## Descrição

Pessoas Permitidas no Local Físico Controlado

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |
| IdtPes | String(023) | Não | Identificador da Pessoa |
| DatIni | Date | Não | Data e Hora Inicial do Registro |
| NomPes | String(040) | Sim | Nome da Pessoa |
| DatFim | Date | Sim | Data e Hora Final do Registro |
| StaAtu | Number(001,0) | Sim | Status do Histórico |
| TipPer | Number(001,0) | Não | Tipo de usuário que concedeu a permissão de acesso à pessoa |

---

## Chave Primária

- VerPlf
- CodPlf
- IdtPes
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
