# R050OCO

## Descrição

Compromissos - Ocorrências

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCom | Number(004,0) | Não | Código do Compromisso |
| CodGru | Number(004,0) | Não | Código do Grupo |
| TipCal | Number(002,0) | Não | Tipo do Cálculo |
| IniOco | Date | Não | Data de Início da Ocorrência |
| SeqOco | Number(004,0) | Não | Sequência da ocorrência |
| FimOco | Date | Sim | Data de Fim da Ocorrência |
| IniExe | Date | Sim | Data Inicial para Execução do Processo |
| FimExe | Date | Sim | Data Final para Execução do Processo |
| QtdDia | Number(003,0) | Sim | Qtd. de Dias Antes da Data de Pagto/Início Férias |
| StaOco | Number(001,0) | Sim | Status da Ocorrência |
| DatCon | Date | Sim | Data de Conclusão da Ocorrência |
| UsuCon | Number(010,0) | Sim | Código do Usuário que Concluiu a Ocorrência |
| ObsOco | String(500) | Sim | Inserir observação da proposta |

---

## Chave Primária

- CodCom
- CodGru
- TipCal
- IniOco
- SeqOco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R050OCO_000

**Tabela:** R050COM

| Origem | Destino |
|--------|---------|
| CodCom | CodCom |

