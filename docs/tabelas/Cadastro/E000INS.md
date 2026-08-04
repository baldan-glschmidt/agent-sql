# E000INS

## Descrição

Insight Control - Controle de Insights

---

## Resumo

- Campos: 15
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| HasHid | String(050) | Não | Hash da mensagem conforme Insight Control |
| DesIns | String(060) | Sim | Descrição do Insight |
| PerExc | Number(001,0) | Não | Periodicidade de execução |
| DiaIni | Number(002,0) | Sim | Dia de início de execução |
| FinVaz | String(001) | Sim | Finalizar na competência após voltar vazio |
| TxtSql | String(4000) | Sim | Select responsável pela extração das informações do Insight |
| CodRgr | Number(004,0) | Sim | Código da Regra responsável pela extração das informações do Insight |
| DatPro | Date | Sim | Data da Próxima Execução |
| HorPro | Number(005,0) | Sim | Hora da Próxima Execução |
| EnvIsc | String(001) | Sim | Enviar para o Insight Control |
| TagPro | String(200) | Sim | Rótulos para validação da exibição da notificação interna |
| VerHtm | String(010) | Sim | Versão do HTML de Notificação |
| TxtHtm | String(5999) | Sim | Conteúdo do HTML de Notificação |
| SitIns | String(001) | Não | Situação do Insight |
| TxtReg | Image | Sim | Conteúdo da regra que será executada |

---

## Chave Primária

- HasHid

---

## Índices

### E000INSIndice1

**Tipo:** Não unico

Campos:
- DatPro
- HorPro

---

## Relacionamentos

Nenhum relacionamento cadastrado.
