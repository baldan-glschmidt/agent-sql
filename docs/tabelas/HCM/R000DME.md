# R000DME

## Descrição

Definições do Motor eSocial

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| ProMot | Number(001,0) | Sim | Tipo de Processamento |
| UrlDoc | String(255) | Sim | URL para conexão com o eDocs |
| UsuDoc | String(100) | Sim | Usuário para conexão com o eDocs |
| SenDoc | String(100) | Sim | Senha para conexão com o eDocs |
| NumIns | Number(014,0) | Sim | Número de CNPJ/CPF da Inscrição do Certificado Digital |
| CfjIns | String(014) | Sim | Número de CNPJ/CPF da Inscrição do Certificado Digital |
| DirArq | String(255) | Sim | Diretório onde serão salvos os arquivos XML |
| GerLog | String(001) | Não | Gerar Arquivos de Log |
| DirLog | String(255) | Sim | Diretório onde serão salvos os arquivos de Log |
| TamLot | Number(004,0) | Sim | Quantidade de pendências que serão tratados em cada lote |
| TemExe | Number(003,0) | Sim | Tempo máximo que uma instância pode levar para processar um lote |
| TemVer | Number(003,0) | Sim | Intervalo de tempo entre cada verificação das pendências |
| TipAmb | Number(001,0) | Sim | Tipo de Ambiente eSocial |
| UsaEdo | String(001) | Sim | Usa eDocs Senior |
| GerGrf | String(001) | Sim | Habilitar GRFGTS - obsoleto |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
