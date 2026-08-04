# E000IPA

## Descrição

Insight de Processos Automáticos

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodIsg | Number(009,0) | Não | Identificador de registro |
| DesIsg | String(060) | Não | Descrição do insight do processo automático |
| TipPra | Number(002,0) | Não | Tipo do processo automático |
| EmpExe | Number(004,0) | Sim | Código da empresa onde o processo automático será executado |
| FilExe | Number(005,0) | Sim | Código da filial onde o processo automático será executado |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| RotSap | Number(003,0) | Não | Rotina do sapiens (tipos de processo: O) |
| NaoSug | String(001) | Sim | Indicativo se deve ou não sugerir novamente este mesmo insight quando reprovado |
| EstIsg | String(001) | Sim | Estado do insight de processo automático |
| PerRsi | Number(005,2) | Sim | Percentual de relevância da sugestão do insight |
| QtdSug | Number(004,0) | Sim | Quantidade de vezes que o insight foi sugerido |
| ParRot | String(999) | Sim | Parâmetros para execução da rotina do Sapiens |

---

## Chave Primária

- CodIsg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
