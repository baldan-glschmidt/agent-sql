# E140LOP

## Descrição

Log de Operações em Notas de Saída

---

## Resumo

- Campos: 26
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| DesLog | String(250) | Sim | Descrição do Log |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| NomUsu | String(255) | Sim | Nome do usuário |
| OrdOpe | String(100) | Sim | Ordem da Operação |
| OpeExe | String(100) | Sim | Operação Executada |
| CplOpe | String(100) | Sim | Complemento da Operação |
| OriLog | String(100) | Sim | Origem do Log |
| CodPra | Number(004,0) | Não | Código do processo automático |
| RotSap | Number(003,0) | Sim | Rotina do Sapiens (tipos de processo: O) |
| WebSap | String(250) | Sim | WebService do Sapiens (Classe do WS) |
| QtdTra | Number(003,0) | Sim | Quantidade de Transações |
| CodCon | String(100) | Sim | Código da Conexão (PID) |
| NomCom | String(100) | Sim | Nome do Computador |
| UsuSop | String(100) | Sim | Usuário do Sistema Operacional |
| ObsReg | String(50000) | Sim | Observação da Regra |
| ObsDep | String(50000) | Sim | Observação de Depuração |
| ObsImg | Image | Sim | Observação em formato Imagem |
| DatGer | Date | Sim | Data da geração |
| HorGer | Number(005,0) | Sim | Hora da geração |
| EmpNfv | Number(004,0) | Não | Código da empresa |
| FilNfv | Number(005,0) | Não | Código da filial |
| SnfNfv | String(003) | Não | Código da série da nota fiscal |
| AbrNfv | String(1000) | Sim | Abrangência de Notas |

---

## Chave Primária

- IdeUni

---

## Índices

### E140LOPIndice1

**Tipo:** Não unico

Campos:
- DatGer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
