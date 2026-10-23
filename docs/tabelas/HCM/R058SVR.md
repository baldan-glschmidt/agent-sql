# R058SVR

## Descrição

Servidores

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
| CodSvr | Number(003,0) | Não | Código do Servidor |
| DesSvr | String(030) | Sim | Descrição do Servidor |
| LnkAcc | String(030) | Sim | Link do Banco p/ Controle On-Line de Acesso |
| LnkRep | String(030) | Sim | Link do Banco p/ Replicação de Dados |
| DirSvr | String(253) | Sim | Diretório no Servidor onde é Executado o Gerenciador On-Line |
| UsuBan | String(020) | Sim | Nome do Usuário de Replicação no Banco |
| SenBan | String(020) | Sim | Senha do Usuário de Replicação no Banco |
| FunSvr | Number(001,0) | Sim | Função do Servidor |
| SesCnx | String(040) | Sim | Sessão e Transação Atual da Conexão |
| TipBan | Number(001,0) | Sim | Tipo de Banco Utilizado |
| DBsBan | String(020) | Sim | Database do Banco |
| ArqIns | String(100) | Sim | Arquivo de instalação (Inst.Ctrl) para conexão dos servidores |
| AmbIns | String(100) | Sim | Ambiente da instalação para conexão dos servidores |
| BasIns | String(100) | Sim | Base de dados da instalação para conexão dos servidores |

---

## Chave Primária

- CodSvr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
