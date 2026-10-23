# R058CEN

## Descrição

Central de Gerenciamento do Acesso

---

## Resumo

- Campos: 28
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCen | Number(002,0) | Não | Central de Gerenciamento do Acesso |
| DesCen | String(030) | Sim | Descrição da Central |
| TipGer | Number(001,0) | Sim | Tipo de Gerenciador |
| DirSvr | String(253) | Sim | Endereço IP ou Hostname/CNAME da Central de Gerenciamento |
| PorCSM | String(016) | Sim | Porta da Concentradora (csm.port.appl) |
| EIPAdp | String(015) | Sim | Endereço IP do Adapter (adapter.ip.app.socket) |
| HorSin | Number(005,0) | Sim | Horário de Sincronização |
| GerSen | String(001) | Sim | Central Gerenciada pela Senior |
| ValUTC | Number(002,0) | Sim | UTC (Fuso Horário) |
| ConsDM | Number(001,0) | Sim | Tipo de Validação |
| IntLot | Number(004,0) | Sim | Intervalo de envio do Lote |
| QtdLot | Number(003,0) | Sim | Quantidade Limite para envio do Lote |
| StaCSM | Number(001,0) | Sim | Status da CSM |
| DirLog | String(200) | Sim | Diretório do log da CSM |
| DirCrp | String(200) | Sim | Diretório do arquivo de criptografia para o BDCC |
| TmpVal | Number(005,0) | Sim | Tempo de validação do autorizador |
| DatUMC | Date | Sim | Data da ultima mensagem da concentradora |
| HorUMC | Number(005,0) | Sim | Hora da ultima mensagem da concentradora |
| SegUMC | Number(002,0) | Sim | Segundo da ultima mensagem da concentradora |
| PorCsl | String(016) | Sim | Porta da Console da Concentradora |
| StaCdm | Number(001,0) | Sim | Estado da carga do Datamart |
| DinCdm | Date | Sim | Data de inicio da carga do Datamart |
| HinCdm | Number(005,0) | Sim | Hora de inicio da carga do Datamart |
| ObsCdm | String(250) | Sim | Observação da carga do Datamart |
| UltCdm | Number(004,0) | Sim | Quantidade minutos para a carga do último datamart |
| TmpLpr | Number(005,0) | Sim | Tempo de Validação LPR |
| ExcPen | String(001) | Sim | Excluir pendência processada com sucesso |
| CenAti | String(001) | Sim | Central de Gerenciamento Ativa |

---

## Chave Primária

- CodCen

---

## Índices

### R058CENIndice2

**Tipo:** Não unico

Campos:
- StaCSM

---

## Relacionamentos

Nenhum relacionamento cadastrado.
