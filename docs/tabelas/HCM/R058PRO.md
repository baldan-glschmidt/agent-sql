# R058PRO

## Descrição

Configuração de Processos Automáticos no Firmware

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdtPro | Number(003,0) | Não | Identificador do Processo |
| DesPro | String(030) | Sim | Descrição do Processo |
| CodSaa | Number(003,0) | Sim | Código do Acionamento |
| DatIni | Date | Sim | Data Inicial da Execução |
| HorIni | Number(005,0) | Sim | Hora Inicial da Execução |
| TipPer | Number(001,0) | Sim | Tipo de Periodicidade |
| PerExe | String(020) | Sim | Periodicidade da Execução |
| TemExe | Number(005,0) | Sim | Tempo de Execução |
| DatVal | Date | Sim | Data de Validade do Processo |
| ExeFer | String(001) | Sim | Executa em feriados |

---

## Chave Primária

- IdtPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
