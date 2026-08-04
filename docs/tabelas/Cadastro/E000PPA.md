# E000PPA

## Descrição

Parâmetros de Insights de Processos Automáticos

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| RotSap | Number(003,0) | Não | Rotina do Sapiens (tipos de processo: 0) |
| QtdExe | Number(004,0) | Sim | Quantidade de execuções do mesmo processo identificado como padrão |
| DiaExe | Number(004,0) | Sim | Período de dias para realizar o monitoramento de insights |
| FrqNtf | Number(004,0) | Sim | Frequência de envio de notificação de novos insights |
| PerMin | Number(005,2) | Sim | Percentual mínimo de precisão para sugestão do insight |
| EmaDes | String(255) | Sim | Endereço dos destinatários que receberão os e-mails da notificação de novos insights |
| EmaAss | String(255) | Sim | Descrição do assunto do e-mail da notificação de novos insights |
| EmaCrp | String(999) | Sim | Texto do e-mail de notificação de novas sugestões de insights |

---

## Chave Primária

- CodEmp
- RotSap

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
