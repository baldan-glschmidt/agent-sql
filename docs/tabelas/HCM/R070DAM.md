# R070DAM

## Descrição

Tabela de Marcações Rejeitadas pelo Coletor

---

## Resumo

- Campos: 44
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DtHLog | Number(014,6) | Sim | Data/Hora do Log do Processamento |
| ICARD | String(012) | Sim | Número do Crachá |
| DIAM | String(002) | Sim | Dia da Marcação |
| MESM | String(002) | Sim | Mês da Marcação |
| ANOM | String(002) | Sim | Ano da Marcação |
| HORAM | String(004) | Sim | Hora da Marcação |
| CODAC | String(003) | Sim | Tipo de Acesso |
| POSIC | String(001) | Sim | Direção do Acesso |
| BLUEB | String(002) | Sim | Centralizadora |
| CODTT | String(002) | Sim | Código do Coletor Alfa |
| END_IP | String(015) | Sim | Número do Endereço IP |
| CODFNC | String(002) | Sim | Código da Função |
| DESLOG | String(254) | Sim | Descrição do Log |
| NOMTAB | String(011) | Sim | Tabela Telemática |
| DATALM | Date | Sim | Data do Alarme |
| ENTALM | String(030) | Sim | Entradas de Alarmes |
| OCOALM | String(030) | Sim | Ocorrências Alarmes |
| NOMLIS | String(015) | Sim | Nome da Lista de Benefícios |
| STABNF | String(001) | Sim | Status do Devedor de Benefício |
| SEGUNDO | String(002) | Sim | Segundo da Marcação |
| VEICULO | String(015) | Sim | Placa do Veículo ou Nome da Lista de Benefícios |
| SOnOff | String(001) | Sim | Status On/Off |
| PESO | Number(009,3) | Sim | Peso da Refeição |
| VALKILO | Number(011,2) | Sim | Valor Kilo da Refeição |
| VALOR | Number(011,2) | Sim | Valor da Refeição |
| QTDE | String(002) | Sim | Quantidade de Sobremesas |
| NIVEL | String(002) | Sim | Nível do Acesso |
| FX_REF | String(002) | Sim | Número da Faixa Horária Refeitório |
| CRED_FX | String(002) | Sim | Qtde de Créditos |
| SITUA | String(002) | Sim | Situação do Crachá |
| QTD_MENS | String(002) | Sim | Qtde. de Mensagens |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| InfAdi | Number(005,0) | Sim | Informação adicional |
| CraAut | String(012) | Sim | Número do crachá da pessoa autorizadora |
| FabMar | Number(002,0) | Sim | Fabricante |
| NumNSR | Number(009,0) | Sim | Número NSR |
| NumRep | String(017) | Sim | Número do REP |
| NumPis | Number(020,0) | Sim | Número do PIS/PASEP |
| NumCpf | Number(020,0) | Sim | Número do CPF |
| Inform | String(299) | Sim | Informações do Registro |
| CodEve | String(003) | Sim | Código do Evento de Alarme (Honeywell) |
| MotRej | Number(001,0) | Sim | Motivo da rejeição da marcação |
| PlaVei | String(010) | Sim | Placa do Veículo |
| IMGLPR | Image | Sim | Imagem LPR |

---

## Chave Primária

Não possui.

---

## Índices

### R070DAMIndice1

**Tipo:** Não unico

Campos:
- DtHLog

---

## Relacionamentos

Nenhum relacionamento cadastrado.
