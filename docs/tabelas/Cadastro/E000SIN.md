# E000SIN

## Descrição

Tabelas - Integrações - Inicialização de integrações

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqSin | Number(009,0) | Não | Número sequencial da inicialização da integração |
| SeqIlr | Number(009,0) | Sim | Número sequencial do registros de inicialização |
| DatIni | Date | Não | Data em que o processo foi inicializado |
| DatFim | Date | Não | Data em que o processo foi finalizado |
| HorIni | Number(005,0) | Sim | Hora de início do processo |
| HorFim | Number(005,0) | Sim | Hora de finalização do processo |
| SitSin | Number(001,0) | Sim | Situação do processo |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pela geração do registro |
| IdeInt | Number(009,0) | Não | Código identificador do tipo de informação |
| DesInt | String(100) | Sim | Descrição da integração inicializada |
| ObsSin | String(250) | Sim | Observações da inicialização |

---

## Chave Primária

- SeqSin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
